from __future__ import division
from models import Player, PlayerBattingSeason
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import Http404
import json


def index(request):
	players = Player.objects.all()[:100]
	
	homeRunLeaders = PlayerBattingSeason.objects.order_by('-Homeruns')[:50]
	
	leaderCareers = []
	leaderIDs = []
	
	for leader in homeRunLeaders:
		
		playerID = leader.Player.PlayerID
		if playerID not in leaderIDs:
			
			seasons = []
			leaderCareer = {
				'id': playerID,
				'seasons': seasons
			}
		
			leaderSeasons = PlayerBattingSeason.objects.filter(Player=leader.Player)
			homeRunSum = 0;
			for season in leaderSeasons:
				homeRunSum += season.Homeruns
				leaderCareer['seasons'].append([season.Year, homeRunSum])
			leaderCareers.append(leaderCareer)
			leaderIDs.append(playerID)
		
	
	leaderCareersJSON = json.dumps(leaderCareers)
	
	return render_to_response('mlb/index.html', 
		{'players': players, 
		'homeRunLeaders': homeRunLeaders,
		'leaderCareersJSON':leaderCareersJSON})
		
def player(request, playerID):
	
	try:
		p = Player.objects.get(pk=playerID)
		seasons = PlayerBattingSeason.objects.filter(Player=playerID).order_by('Year')
		
	except Player.DoesNotExist:
		raise Http404
	
	return render_to_response('mlb/player.html', 
		{'player': p,
		'seasons': seasons})
	