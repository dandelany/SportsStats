from __future__ import division
from django.db import models

# Create your models here.
class Player(models.Model):
	PlayerID = models.CharField(max_length=12)
	PlayerID.primary_key = True
	LahmanID = models.IntegerField()
	
	LastName = models.CharField(max_length=20)
	FirstName = models.CharField(max_length=15)
	GivenName = models.CharField(max_length=50, null=True)
	NickName = models.CharField(max_length=50, null=True)
	NameNote = models.CharField(max_length=127, null=True)
	
	BirthYear = models.IntegerField(null=True)
	BirthMonth = models.IntegerField(null=True)
	BirthDay = models.IntegerField(null=True)
	BirthCountry = models.CharField(max_length=25, null=True)
	BirthState = models.CharField(max_length=2, null=True)
	BirthCity = models.CharField(max_length=32, null=True)
	
	DeathYear = models.IntegerField(null=True)
	DeathMonth = models.IntegerField(null=True)
	DeathDay = models.IntegerField(null=True)
	DeathCountry = models.CharField(max_length=35, null=True)
	DeathState = models.CharField(max_length=2, null=True)
	DeathCity = models.CharField(max_length=32, null=True)
	
	Weight = models.IntegerField(null=True)
	Height = models.IntegerField(null=True)
	
	BatHand = models.CharField(max_length=1, null=True)
	ThrowHand = models.CharField(max_length=1, null=True)
	
	DebutDate = models.CharField(max_length=18, null=True)
	FinalGameDate = models.CharField(max_length=18, null=True)
	
	College = models.CharField(max_length=50, null=True)
	
	def __unicode__(self):
		return self.FirstName + " " + self.LastName


class PlayerBattingSeason(models.Model):
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

class PlayerBattingCareer(models.Model):
	Player = models.ForeignKey(Player)
	
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
		return str(self.Player)