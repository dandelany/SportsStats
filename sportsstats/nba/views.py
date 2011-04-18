from __future__ import division
from models import Team, Game
from django.shortcuts import render_to_response
from django.core import serializers
import json


def index(request):
	teamList = Team.objects.all().order_by('TeamName')
	
	teamStats = []
	for team in teamList:
		thisTeamStats = {
			'id': team.TeamID,
			'name': team.TeamName,
			'wlr': team.getWinLossRatio(),
		}
		thisTeamStats['wlr']['wlr'] = "%.1f"%(thisTeamStats['wlr']['wlr']*100)+"%"
		teamStats.append(thisTeamStats)
	
	
	gameList = Game.objects.all().order_by('GameDate')
	
	teamStatsJSON = json.dumps(teamStats)
	marginListJSON = json.dumps(marginList)
	tieListJSON = json.dumps(tieList)
	marginsByTeamJSON = json.dumps(marginsByTeam)
	leagueSpreadsJSON = json.dumps(leagueSpreads)

	return render_to_response('nba/index.html', {
		'teamStats':teamStats,
		'teamStatsJSON':teamStatsJSON,
		'marginListJSON':marginListJSON,
		'tieListJSON':tieListJSON,
		'marginAvg':marginAvg,
		'marginsByTeamJSON':marginsByTeamJSON,
		'leagueSpreadsJSON':leagueSpreadsJSON
	})
	
	
	
	def addToLeagueSpreads(leagueSpreads, homeSpread):
		if homeSpread in leagueSpreads['dist']['total']:
			leagueSpreads['dist']['total'][homeSpread] += 1
			leagueSpreads['dist']['total'][homeSpread*-1] += 1
		else:
			leagueSpreads['dist']['total'][homeSpread] = 1
			leagueSpreads['dist']['total'][homeSpread*-1] = 1
		
		"""
		if homeSpread in leagueSpreads['dist']['h']:
			leagueSpreads['dist']['h'][homeSpread] += 1
		else:
			leagueSpreads['dist']['h'][homeSpread] = 1
			
		if (homeSpread*-1) in leagueSpreads['dist']['a']:
			leagueSpreads['dist']['a'][homeSpread*-1] += 1
		else:
			leagueSpreads['dist']['a'][homeSpread*-1] = 1
		
		return leagueSpreads
		"""	
	
	def addToTeamDist(teamSpreads, game, team):
		
		marginList = []
		marginDict = {}
		marginSum = 0
		tieList = []
		marginsByTeam = {}
		marginDistByTeam = {}

		leagueSpreads = { 
			'dist': { 'h': {}, 'a': {}, 'total': {} }
		}
		teamSpreads = {
			'hist': {},
			'dist': {}
		}	
	
		for game in gameList:
			thisGameMargin = game.getHomeWinMargin()
	
			leagueSpreads = addToLeagueSpreads(leagueSpreads, thisGameMargin)
	
			teamSpreads = addToTeamDist(teamSpreads, thisGameMargin, game.HomeTeam)
			teamSpreads = addToTeamDist(teamSpreads, thisGameMargin*-1, game.AwayTeam)
	
			# find ties
			if thisGameMargin == 0:
				tieList.append(game.GameID)
		
			# add margin to dict for league histogram
			if thisGameMargin in marginDict:
				marginDict[thisGameMargin] += 1
			else:
				marginDict[thisGameMargin] = 1
		
				
			# add to sum for average	
			marginSum += thisGameMargin
	
			# add to team dictionary for w/l spark
			if game.HomeTeam.pk in marginsByTeam:
				marginsByTeam[game.HomeTeam.pk].append(thisGameMargin)
			else:
				marginsByTeam[game.HomeTeam.pk] = [thisGameMargin]
		
			if game.AwayTeam.pk in marginsByTeam:
				marginsByTeam[game.AwayTeam.pk].append(thisGameMargin*-1)
			else:
				marginsByTeam[game.AwayTeam.pk] = [thisGameMargin*-1]
	

		marginAvg = marginSum/len(gameList)

		for key,value in marginDict.items():
			marginList.append([key,value])


	
