# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'PlayerBattingCareerPercentile.SacrificeHits'
        db.alter_column('mlb_playerbattingcareerpercentile', 'SacrificeHits', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.Runs'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Runs', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.RunsBattedIn'
        db.alter_column('mlb_playerbattingcareerpercentile', 'RunsBattedIn', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.Triples'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Triples', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.Strikeouts'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Strikeouts', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.StolenBases'
        db.alter_column('mlb_playerbattingcareerpercentile', 'StolenBases', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.SacrificeFlies'
        db.alter_column('mlb_playerbattingcareerpercentile', 'SacrificeFlies', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.Hits'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Hits', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.IntentionalWalks'
        db.alter_column('mlb_playerbattingcareerpercentile', 'IntentionalWalks', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.Doubles'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Doubles', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.GroundedIntoDouble'
        db.alter_column('mlb_playerbattingcareerpercentile', 'GroundedIntoDouble', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.HitByPitch'
        db.alter_column('mlb_playerbattingcareerpercentile', 'HitByPitch', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.Homeruns'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Homeruns', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.BaseOnBalls'
        db.alter_column('mlb_playerbattingcareerpercentile', 'BaseOnBalls', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'PlayerBattingCareerPercentile.CaughtStealing'
        db.alter_column('mlb_playerbattingcareerpercentile', 'CaughtStealing', self.gf('django.db.models.fields.FloatField')())


    def backwards(self, orm):
        
        # Changing field 'PlayerBattingCareerPercentile.SacrificeHits'
        db.alter_column('mlb_playerbattingcareerpercentile', 'SacrificeHits', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.Runs'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Runs', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.RunsBattedIn'
        db.alter_column('mlb_playerbattingcareerpercentile', 'RunsBattedIn', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.Triples'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Triples', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.Strikeouts'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Strikeouts', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.StolenBases'
        db.alter_column('mlb_playerbattingcareerpercentile', 'StolenBases', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.SacrificeFlies'
        db.alter_column('mlb_playerbattingcareerpercentile', 'SacrificeFlies', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.Hits'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Hits', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.IntentionalWalks'
        db.alter_column('mlb_playerbattingcareerpercentile', 'IntentionalWalks', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.Doubles'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Doubles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.GroundedIntoDouble'
        db.alter_column('mlb_playerbattingcareerpercentile', 'GroundedIntoDouble', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.HitByPitch'
        db.alter_column('mlb_playerbattingcareerpercentile', 'HitByPitch', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.Homeruns'
        db.alter_column('mlb_playerbattingcareerpercentile', 'Homeruns', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.BaseOnBalls'
        db.alter_column('mlb_playerbattingcareerpercentile', 'BaseOnBalls', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'PlayerBattingCareerPercentile.CaughtStealing'
        db.alter_column('mlb_playerbattingcareerpercentile', 'CaughtStealing', self.gf('django.db.models.fields.IntegerField')())


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
        'mlb.playerbattingcareerperab': {
            'AtBats': ('django.db.models.fields.IntegerField', [], {}),
            'BaseOnBalls': ('django.db.models.fields.FloatField', [], {}),
            'CaughtStealing': ('django.db.models.fields.FloatField', [], {}),
            'Doubles': ('django.db.models.fields.FloatField', [], {}),
            'GroundedIntoDouble': ('django.db.models.fields.FloatField', [], {}),
            'HitByPitch': ('django.db.models.fields.FloatField', [], {}),
            'Hits': ('django.db.models.fields.FloatField', [], {}),
            'Homeruns': ('django.db.models.fields.FloatField', [], {}),
            'IntentionalWalks': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'PlayerBattingCareerPerAB'},
            'Player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mlb.Player']"}),
            'Runs': ('django.db.models.fields.FloatField', [], {}),
            'RunsBattedIn': ('django.db.models.fields.FloatField', [], {}),
            'SacrificeFlies': ('django.db.models.fields.FloatField', [], {}),
            'SacrificeHits': ('django.db.models.fields.FloatField', [], {}),
            'StolenBases': ('django.db.models.fields.FloatField', [], {}),
            'Strikeouts': ('django.db.models.fields.FloatField', [], {}),
            'Triples': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mlb.playerbattingcareerpercentile': {
            'AtBats': ('django.db.models.fields.IntegerField', [], {}),
            'BaseOnBalls': ('django.db.models.fields.FloatField', [], {}),
            'CaughtStealing': ('django.db.models.fields.FloatField', [], {}),
            'Doubles': ('django.db.models.fields.FloatField', [], {}),
            'Games': ('django.db.models.fields.IntegerField', [], {}),
            'GamesBatting': ('django.db.models.fields.IntegerField', [], {}),
            'GroundedIntoDouble': ('django.db.models.fields.FloatField', [], {}),
            'HitByPitch': ('django.db.models.fields.FloatField', [], {}),
            'Hits': ('django.db.models.fields.FloatField', [], {}),
            'Homeruns': ('django.db.models.fields.FloatField', [], {}),
            'IntentionalWalks': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'PlayerBattingCareerPercentile'},
            'Percentile': ('django.db.models.fields.IntegerField', [], {}),
            'Runs': ('django.db.models.fields.FloatField', [], {}),
            'RunsBattedIn': ('django.db.models.fields.FloatField', [], {}),
            'SacrificeFlies': ('django.db.models.fields.FloatField', [], {}),
            'SacrificeHits': ('django.db.models.fields.FloatField', [], {}),
            'StolenBases': ('django.db.models.fields.FloatField', [], {}),
            'Strikeouts': ('django.db.models.fields.FloatField', [], {}),
            'Triples': ('django.db.models.fields.FloatField', [], {}),
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
