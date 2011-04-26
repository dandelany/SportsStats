# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Player.GivenName'
        db.add_column('mlb_player', 'GivenName', self.gf('django.db.models.fields.CharField')(max_length=50, null=True), keep_default=False)

        # Adding field 'Player.NickName'
        db.add_column('mlb_player', 'NickName', self.gf('django.db.models.fields.CharField')(max_length=50, null=True), keep_default=False)

        # Adding field 'Player.NameNote'
        db.add_column('mlb_player', 'NameNote', self.gf('django.db.models.fields.CharField')(max_length=127, null=True), keep_default=False)

        # Adding field 'Player.BirthYear'
        db.add_column('mlb_player', 'BirthYear', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.BirthMonth'
        db.add_column('mlb_player', 'BirthMonth', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.BirthDay'
        db.add_column('mlb_player', 'BirthDay', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.BirthCountry'
        db.add_column('mlb_player', 'BirthCountry', self.gf('django.db.models.fields.CharField')(max_length=25, null=True), keep_default=False)

        # Adding field 'Player.BirthState'
        db.add_column('mlb_player', 'BirthState', self.gf('django.db.models.fields.CharField')(max_length=2, null=True), keep_default=False)

        # Adding field 'Player.BirthCity'
        db.add_column('mlb_player', 'BirthCity', self.gf('django.db.models.fields.CharField')(max_length=32, null=True), keep_default=False)

        # Adding field 'Player.DeathYear'
        db.add_column('mlb_player', 'DeathYear', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.DeathMonth'
        db.add_column('mlb_player', 'DeathMonth', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.DeathDay'
        db.add_column('mlb_player', 'DeathDay', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.DeathCountry'
        db.add_column('mlb_player', 'DeathCountry', self.gf('django.db.models.fields.CharField')(max_length=35, null=True), keep_default=False)

        # Adding field 'Player.DeathState'
        db.add_column('mlb_player', 'DeathState', self.gf('django.db.models.fields.CharField')(max_length=2, null=True), keep_default=False)

        # Adding field 'Player.DeathCity'
        db.add_column('mlb_player', 'DeathCity', self.gf('django.db.models.fields.CharField')(max_length=32, null=True), keep_default=False)

        # Adding field 'Player.Weight'
        db.add_column('mlb_player', 'Weight', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.Height'
        db.add_column('mlb_player', 'Height', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Player.BatHand'
        db.add_column('mlb_player', 'BatHand', self.gf('django.db.models.fields.CharField')(max_length=1, null=True), keep_default=False)

        # Adding field 'Player.ThrowHand'
        db.add_column('mlb_player', 'ThrowHand', self.gf('django.db.models.fields.CharField')(max_length=1, null=True), keep_default=False)

        # Adding field 'Player.DebutDate'
        db.add_column('mlb_player', 'DebutDate', self.gf('django.db.models.fields.CharField')(max_length=18, null=True), keep_default=False)

        # Adding field 'Player.FinalGameDate'
        db.add_column('mlb_player', 'FinalGameDate', self.gf('django.db.models.fields.CharField')(max_length=18, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Player.GivenName'
        db.delete_column('mlb_player', 'GivenName')

        # Deleting field 'Player.NickName'
        db.delete_column('mlb_player', 'NickName')

        # Deleting field 'Player.NameNote'
        db.delete_column('mlb_player', 'NameNote')

        # Deleting field 'Player.BirthYear'
        db.delete_column('mlb_player', 'BirthYear')

        # Deleting field 'Player.BirthMonth'
        db.delete_column('mlb_player', 'BirthMonth')

        # Deleting field 'Player.BirthDay'
        db.delete_column('mlb_player', 'BirthDay')

        # Deleting field 'Player.BirthCountry'
        db.delete_column('mlb_player', 'BirthCountry')

        # Deleting field 'Player.BirthState'
        db.delete_column('mlb_player', 'BirthState')

        # Deleting field 'Player.BirthCity'
        db.delete_column('mlb_player', 'BirthCity')

        # Deleting field 'Player.DeathYear'
        db.delete_column('mlb_player', 'DeathYear')

        # Deleting field 'Player.DeathMonth'
        db.delete_column('mlb_player', 'DeathMonth')

        # Deleting field 'Player.DeathDay'
        db.delete_column('mlb_player', 'DeathDay')

        # Deleting field 'Player.DeathCountry'
        db.delete_column('mlb_player', 'DeathCountry')

        # Deleting field 'Player.DeathState'
        db.delete_column('mlb_player', 'DeathState')

        # Deleting field 'Player.DeathCity'
        db.delete_column('mlb_player', 'DeathCity')

        # Deleting field 'Player.Weight'
        db.delete_column('mlb_player', 'Weight')

        # Deleting field 'Player.Height'
        db.delete_column('mlb_player', 'Height')

        # Deleting field 'Player.BatHand'
        db.delete_column('mlb_player', 'BatHand')

        # Deleting field 'Player.ThrowHand'
        db.delete_column('mlb_player', 'ThrowHand')

        # Deleting field 'Player.DebutDate'
        db.delete_column('mlb_player', 'DebutDate')

        # Deleting field 'Player.FinalGameDate'
        db.delete_column('mlb_player', 'FinalGameDate')


    models = {
        'mlb.player': {
            'BatHand': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'BirthCity': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'BirthCountry': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'BirthDay': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'BirthMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'BirthState': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'BirthYear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
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
