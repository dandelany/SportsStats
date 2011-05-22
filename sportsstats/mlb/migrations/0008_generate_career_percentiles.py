# encoding: utf-8
import datetime, math
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
		PLAYERBATTINGCAREER_FIELDS = [
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
		
		ptileDict = {}
		
		for field in PLAYERBATTINGCAREER_FIELDS:
			if field['fieldName'] != 'Player':
				
				print('calculating ' + field['longName'] + ' percentiles...')
				
				pTiles = [0] * 100
				gteOneFilter = {field['fieldName'] + '__gte': 1}
				numGoodCareers = orm.PlayerBattingCareer.objects.filter(**gteOneFilter).count()
				pTileSize = math.floor(numGoodCareers/100)
				
				pTileMinIndex = pTileSize
				for i in range(100, 0, -1):
					if i == 1:
						pTileMinIndex = orm.PlayerBattingCareer.objects.all().count() - 1
					
					pTileMinPlayer = orm.PlayerBattingCareer.objects.order_by('-'+field['fieldName'])[pTileMinIndex-1:pTileMinIndex].values()
					
					pTileMinValue = pTileMinPlayer[0][field['fieldName']]
					pTiles[i-1] = pTileMinValue
					
					pTileMinIndex += pTileSize
				
				ptileDict[field['fieldName']] = pTiles
		
		for i in range(0,100):
			pTile = orm.PlayerBattingCareerPercentile.objects.create(
				Percentile = i,
				Homeruns = ptileDict['Homeruns'][i],
				Games = ptileDict['Games'][i],
				GamesBatting = ptileDict['GamesBatting'][i],
				AtBats = ptileDict['AtBats'][i],
				Runs = ptileDict['Runs'][i],
				Hits = ptileDict['Hits'][i],
				Doubles = ptileDict['Doubles'][i],
				Triples = ptileDict['Triples'][i],
				RunsBattedIn = ptileDict['RunsBattedIn'][i],
				StolenBases = ptileDict['StolenBases'][i],
				CaughtStealing = ptileDict['CaughtStealing'][i],
				BaseOnBalls = ptileDict['BaseOnBalls'][i],
				Strikeouts = ptileDict['Strikeouts'][i],
				IntentionalWalks = ptileDict['IntentionalWalks'][i],
				HitByPitch = ptileDict['HitByPitch'][i],
				SacrificeHits = ptileDict['SacrificeHits'][i],
				SacrificeFlies = ptileDict['SacrificeFlies'][i],
				GroundedIntoDouble = ptileDict['GroundedIntoDouble'][i]
			)


    def backwards(self, orm):
        orm.PlayerBattingCareerPercentile.objects.all().delete()


    models = {
        'mlb.player': {
            'BatHand': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'BirthCity': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'BirthCountry': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'BirthDay': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'BirthMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'BirthState': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'BirthYear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'College': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'DeathCity': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'DeathCountry': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True'}),
            'DeathDay': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'DeathMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'DeathState': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'DeathYear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'DebutDate': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True'}),
            'FinalGameDate': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True'}),
            'FirstName': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'GivenName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'Height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'LahmanID': ('django.db.models.fields.IntegerField', [], {}),
            'LastName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Meta': {'object_name': 'Player'},
            'NameNote': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True'}),
            'NickName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'PlayerID': ('django.db.models.fields.CharField', [], {'max_length': '12', 'primary_key': 'True'}),
            'ThrowHand': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'Weight': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'mlb.playerbattingcareer': {
            'AtBats': ('django.db.models.fields.IntegerField', [], {}),
            'BaseOnBalls': ('django.db.models.fields.IntegerField', [], {}),
            'CaughtStealing': ('django.db.models.fields.IntegerField', [], {}),
            'Doubles': ('django.db.models.fields.IntegerField', [], {}),
            'Games': ('django.db.models.fields.IntegerField', [], {}),
            'GamesBatting': ('django.db.models.fields.IntegerField', [], {}),
            'GroundedIntoDouble': ('django.db.models.fields.IntegerField', [], {}),
            'HitByPitch': ('django.db.models.fields.IntegerField', [], {}),
            'Hits': ('django.db.models.fields.IntegerField', [], {}),
            'Homeruns': ('django.db.models.fields.IntegerField', [], {}),
            'IntentionalWalks': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'PlayerBattingCareer'},
            'Player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mlb.Player']"}),
            'Runs': ('django.db.models.fields.IntegerField', [], {}),
            'RunsBattedIn': ('django.db.models.fields.IntegerField', [], {}),
            'SacrificeFlies': ('django.db.models.fields.IntegerField', [], {}),
            'SacrificeHits': ('django.db.models.fields.IntegerField', [], {}),
            'StolenBases': ('django.db.models.fields.IntegerField', [], {}),
            'Strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'Triples': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mlb.playerbattingcareerpercentile': {
            'AtBats': ('django.db.models.fields.IntegerField', [], {}),
            'BaseOnBalls': ('django.db.models.fields.IntegerField', [], {}),
            'CaughtStealing': ('django.db.models.fields.IntegerField', [], {}),
            'Doubles': ('django.db.models.fields.IntegerField', [], {}),
            'Games': ('django.db.models.fields.IntegerField', [], {}),
            'GamesBatting': ('django.db.models.fields.IntegerField', [], {}),
            'GroundedIntoDouble': ('django.db.models.fields.IntegerField', [], {}),
            'HitByPitch': ('django.db.models.fields.IntegerField', [], {}),
            'Hits': ('django.db.models.fields.IntegerField', [], {}),
            'Homeruns': ('django.db.models.fields.IntegerField', [], {}),
            'IntentionalWalks': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'PlayerBattingCareerPercentile'},
            'Percentile': ('django.db.models.fields.IntegerField', [], {}),
            'Runs': ('django.db.models.fields.IntegerField', [], {}),
            'RunsBattedIn': ('django.db.models.fields.IntegerField', [], {}),
            'SacrificeFlies': ('django.db.models.fields.IntegerField', [], {}),
            'SacrificeHits': ('django.db.models.fields.IntegerField', [], {}),
            'StolenBases': ('django.db.models.fields.IntegerField', [], {}),
            'Strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'Triples': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mlb.playerbattingseason': {
            'AtBats': ('django.db.models.fields.IntegerField', [], {}),
            'BaseOnBalls': ('django.db.models.fields.IntegerField', [], {}),
            'CaughtStealing': ('django.db.models.fields.IntegerField', [], {}),
            'Doubles': ('django.db.models.fields.IntegerField', [], {}),
            'Games': ('django.db.models.fields.IntegerField', [], {}),
            'GamesBatting': ('django.db.models.fields.IntegerField', [], {}),
            'GroundedIntoDouble': ('django.db.models.fields.IntegerField', [], {}),
            'HitByPitch': ('django.db.models.fields.IntegerField', [], {}),
            'Hits': ('django.db.models.fields.IntegerField', [], {}),
            'Homeruns': ('django.db.models.fields.IntegerField', [], {}),
            'IntentionalWalks': ('django.db.models.fields.IntegerField', [], {}),
            'LeagueID': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'Meta': {'object_name': 'PlayerBattingSeason'},
            'Player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mlb.Player']"}),
            'Runs': ('django.db.models.fields.IntegerField', [], {}),
            'RunsBattedIn': ('django.db.models.fields.IntegerField', [], {}),
            'SacrificeFlies': ('django.db.models.fields.IntegerField', [], {}),
            'SacrificeHits': ('django.db.models.fields.IntegerField', [], {}),
            'Stint': ('django.db.models.fields.IntegerField', [], {}),
            'StolenBases': ('django.db.models.fields.IntegerField', [], {}),
            'Strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'TeamID': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'Triples': ('django.db.models.fields.IntegerField', [], {}),
            'Year': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mlb']
