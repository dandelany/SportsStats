# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Player.College'
        db.add_column('mlb_player', 'College', self.gf('django.db.models.fields.CharField')(max_length=50, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Player.College'
        db.delete_column('mlb_player', 'College')


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
        'mlb.playerbatting': {
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
            'Meta': {'object_name': 'PlayerBatting'},
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
