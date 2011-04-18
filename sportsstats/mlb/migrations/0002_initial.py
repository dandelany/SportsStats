# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Player'
        db.create_table('mlb_player', (
            ('PlayerID', self.gf('django.db.models.fields.CharField')(max_length=12, primary_key=True)),
            ('LahmanID', self.gf('django.db.models.fields.IntegerField')()),
            ('LastName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('FirstName', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('mlb', ['Player'])

        # Adding model 'PlayerBatting'
        db.create_table('mlb_playerbatting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mlb.Player'])),
            ('Year', self.gf('django.db.models.fields.IntegerField')()),
            ('Stint', self.gf('django.db.models.fields.IntegerField')()),
            ('TeamID', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('LeagueID', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('Games', self.gf('django.db.models.fields.IntegerField')()),
            ('GamesBatting', self.gf('django.db.models.fields.IntegerField')()),
            ('AtBats', self.gf('django.db.models.fields.IntegerField')()),
            ('Runs', self.gf('django.db.models.fields.IntegerField')()),
            ('Hits', self.gf('django.db.models.fields.IntegerField')()),
            ('Doubles', self.gf('django.db.models.fields.IntegerField')()),
            ('Triples', self.gf('django.db.models.fields.IntegerField')()),
            ('Homeruns', self.gf('django.db.models.fields.IntegerField')()),
            ('RunsBattedIn', self.gf('django.db.models.fields.IntegerField')()),
            ('StolenBases', self.gf('django.db.models.fields.IntegerField')()),
            ('CaughtStealing', self.gf('django.db.models.fields.IntegerField')()),
            ('BaseOnBalls', self.gf('django.db.models.fields.IntegerField')()),
            ('Strikeouts', self.gf('django.db.models.fields.IntegerField')()),
            ('IntentionalWalks', self.gf('django.db.models.fields.IntegerField')()),
            ('HitByPitch', self.gf('django.db.models.fields.IntegerField')()),
            ('SacrificeHits', self.gf('django.db.models.fields.IntegerField')()),
            ('SacrificeFlies', self.gf('django.db.models.fields.IntegerField')()),
            ('GroundedIntoDouble', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mlb', ['PlayerBatting'])


    def backwards(self, orm):
        
        # Deleting model 'Player'
        db.delete_table('mlb_player')

        # Deleting model 'PlayerBatting'
        db.delete_table('mlb_playerbatting')


    models = {
        'mlb.player': {
            'FirstName': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'LahmanID': ('django.db.models.fields.IntegerField', [], {}),
            'LastName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Meta': {'object_name': 'Player'},
            'PlayerID': ('django.db.models.fields.CharField', [], {'max_length': '12', 'primary_key': 'True'})
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
