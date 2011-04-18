from __future__ import division
from django.db import models

# Create your models here.
class Player(models.Model):
	PlayerID = models.CharField(max_length=12)
	PlayerID.primary_key = True
	
	LahmanID = models.IntegerField()
	
	LastName = models.CharField(max_length=20)
	FirstName = models.CharField(max_length=15)
	
	def __unicode__(self):
		return self.FirstName + " " + self.LastName

class PlayerBatting(models.Model):
	Player = models.ForeignKey(Player)
	
	Year = models.IntegerField()
	Stint = models.IntegerField()
	TeamID = models.CharField(max_length=4)
	LeagueID = models.CharField(max_length=2)
	
	Games = models.IntegerField()
	GamesBatting = models.IntegerField()
	AtBats = models.IntegerField()
	Runs = models.IntegerField()
	Hits = models.IntegerField()
	Doubles = models.IntegerField()
	Triples = models.IntegerField()
	Homeruns = models.IntegerField()
	RunsBattedIn = models.IntegerField()
	StolenBases = models.IntegerField()
	CaughtStealing = models.IntegerField()
	BaseOnBalls = models.IntegerField()
	Strikeouts = models.IntegerField()
	IntentionalWalks = models.IntegerField()
	HitByPitch = models.IntegerField()
	SacrificeHits = models.IntegerField()
	SacrificeFlies = models.IntegerField()
	GroundedIntoDouble = models.IntegerField()
	
	def __unicode__(self):
		return str(self.Year) + " " + str(self.Player)