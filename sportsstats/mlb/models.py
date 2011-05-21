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
	
	def getCareerStats(self, column, isCumulative):
		seasons = []
		career = {
			'id': self.PlayerID,
			'name': self.FirstName + " " + self.LastName,
			'seasons': seasons
		}
		
		allSeasons = PlayerBattingSeason.objects.filter(Player=self).values(column, 'Year')
		colSum = 0;
		for season in allSeasons:
			colSum += season[column]
			dataToAdd = colSum if isCumulative else season[column]
			career['seasons'].append([season['Year'], dataToAdd])
		
		career['total'] = colSum;
		return career
	
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
	
	FIELDS = [
		{ 'abbrev': 'Year', 'fieldName': 'Year' },
		{ 'abbrev': 'Games', 'fieldName': 'Games' },
		{ 'abbrev': 'GBatting', 'fieldName': 'GamesBatting' },
		{ 'abbrev': 'AB', 'fieldName': 'AtBats' },
		{ 'abbrev': 'R', 'fieldName': 'Runs' },
		{ 'abbrev': 'H', 'fieldName': 'Hits' },
		{ 'abbrev': 'D', 'fieldName': 'Doubles' },
		{ 'abbrev': 'T', 'fieldName': 'Triples' },
		{ 'abbrev': 'HR', 'fieldName': 'Homeruns' },
		{ 'abbrev': 'RBI', 'fieldName': 'RunsBattedIn' },
		{ 'abbrev': 'SB', 'fieldName': 'StolenBases' },
		{ 'abbrev': 'CS', 'fieldName': 'CaughtStealing' },
		{ 'abbrev': 'BOB', 'fieldName': 'BaseOnBalls' },
		{ 'abbrev': 'SO', 'fieldName': 'Strikeouts' },
		{ 'abbrev': 'IW', 'fieldName': 'IntentionalWalks' },
		{ 'abbrev': 'HBP', 'fieldName': 'HitByPitch' },
		{ 'abbrev': 'SH', 'fieldName': 'SacrificeHits' },
		{ 'abbrev': 'SF', 'fieldName': 'SacrificeFlies' },
		{ 'abbrev': 'GIDP', 'fieldName': 'GroundedIntoDouble' }
	]
	
	def fieldLookup(self, key, value):
		def find(f, seq):
			"""Return first item in sequence where f(item) == True."""
			for item in seq:
				if f(item): 
					return item
			return false
		
		return find(lambda field: field[key] == value, self.FIELDS)
	
	def __unicode__(self):
		return str(self.Year) + " " + str(self.Player)

class PlayerBattingCareer(models.Model):
	Player = models.ForeignKey(Player, verbose_name='Player')
	
	Games = models.IntegerField(verbose_name='G')
	GamesBatting = models.IntegerField(verbose_name='GBatting')
	AtBats = models.IntegerField(verbose_name='AB')
	Runs = models.IntegerField(verbose_name='R')
	Hits = models.IntegerField(verbose_name='H')
	Doubles = models.IntegerField(verbose_name='D')
	Triples = models.IntegerField(verbose_name='T')
	Homeruns = models.IntegerField(verbose_name='HR')
	RunsBattedIn = models.IntegerField(verbose_name='RBI')
	StolenBases = models.IntegerField(verbose_name='SB')
	CaughtStealing = models.IntegerField(verbose_name='CS')
	BaseOnBalls = models.IntegerField(verbose_name='BOB')
	Strikeouts = models.IntegerField(verbose_name='SO')
	IntentionalWalks = models.IntegerField(verbose_name='IW')
	HitByPitch = models.IntegerField(verbose_name='HBP')
	SacrificeHits = models.IntegerField(verbose_name='SH')
	SacrificeFlies = models.IntegerField(verbose_name='SF')
	GroundedIntoDouble = models.IntegerField(verbose_name='GIDP')
	
	FIELDS = [
		{ 'abbrev': 'Player', 'fieldName': 'Player', 'longName': 'Player' },
		{ 'abbrev': 'Games', 'fieldName': 'Games', 'longName': 'Games Played' },
		{ 'abbrev': 'GBatting', 'fieldName': 'GamesBatting', 'longName': 'Games Batted' },
		{ 'abbrev': 'AB', 'fieldName': 'AtBats', 'longName': 'At Bats' },
		{ 'abbrev': 'R', 'fieldName': 'Runs', 'longName': 'Runs' },
		{ 'abbrev': 'H', 'fieldName': 'Hits', 'longName': 'Hits' },
		{ 'abbrev': 'D', 'fieldName': 'Doubles', 'longName': 'Doubles' },
		{ 'abbrev': 'T', 'fieldName': 'Triples', 'longName': 'Triples' },
		{ 'abbrev': 'HR', 'fieldName': 'Homeruns', 'longName': 'Home Runs' },
		{ 'abbrev': 'RBI', 'fieldName': 'RunsBattedIn', 'longName': 'Runs Batted In' },
		{ 'abbrev': 'SB', 'fieldName': 'StolenBases', 'longName': 'Stolen Bases' },
		{ 'abbrev': 'CS', 'fieldName': 'CaughtStealing', 'longName': 'Caught Stealing' },
		{ 'abbrev': 'BOB', 'fieldName': 'BaseOnBalls', 'longName': 'Base On Balls' },
		{ 'abbrev': 'SO', 'fieldName': 'Strikeouts', 'longName': 'Strikeouts' },
		{ 'abbrev': 'IW', 'fieldName': 'IntentionalWalks', 'longName': 'Intentional Walks' },
		{ 'abbrev': 'HBP', 'fieldName': 'HitByPitch', 'longName': 'Hit By Pitch' },
		{ 'abbrev': 'SH', 'fieldName': 'SacrificeHits', 'longName': 'Sacrifice Hits' },
		{ 'abbrev': 'SF', 'fieldName': 'SacrificeFlies', 'longName': 'Sacrifice Flies' },
		{ 'abbrev': 'GIDP', 'fieldName': 'GroundedIntoDouble', 'longName': 'Grounded Into Double Play' }
	]
	
	@classmethod
	def fieldLookup(cls, key, value):
		def find(f, seq):
			"""Return first item in sequence where f(item) == True."""
			for item in seq:
				if f(item): 
					return item
			return False
		
		return find(lambda field: field[key] == value, cls.FIELDS)

	def __unicode__(self):
		return str(self.Player)