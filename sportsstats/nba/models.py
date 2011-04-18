from __future__ import division
from django.db import models


# nba_team
class Team(models.Model):
	TeamID = models.CharField(max_length=3)
	TeamID.primary_key = True
	
	TeamName = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.TeamName
	
	def getWinLossRatio(self):
		wins = 0
		losses = 0
		ties = 0
		
		for game in self.HomeGames.all():
			if(game.HomeScore > game.AwayScore):
				wins += 1
			elif(game.HomeScore < game.AwayScore):
				losses += 1
			else:
				ties += 1
		
		for game in self.AwayGames.all():
			if(game.AwayScore > game.HomeScore):
				wins += 1
			elif(game.HomeScore < game.AwayScore):
				losses += 1
			else:
				ties += 1
		
		return {
			'w': wins,
			'l': losses,
			't': ties,
			'wlr': wins/(wins+losses+ties)
		}

# nba_game
class Game(models.Model):
	GameID = models.CharField(max_length=15)
	GameID.primary_key = True
	
	GameDate = models.DateField()
	
	HomeTeam = models.ForeignKey(Team, related_name='HomeGames')
	
	HomeScore = models.IntegerField()
	HomeScore.default = -1
	
	AwayTeam = models.ForeignKey(Team, related_name='AwayGames')
	
	AwayScore = models.IntegerField()
	AwayScore.default = -1
	
	def __unicode__(self):
		return self.GameID
	
	def getHomeWinMargin(self):
		return self.HomeScore - self.AwayScore
