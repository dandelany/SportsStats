from __future__ import division
from models import Player, PlayerBatting
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import Http404
import json


def index(request):
	players = Player.objects.all()[:100]
	
	homeRunLeaders = PlayerBatting.objects.order_by('-Homeruns')[:50]
	
	return render_to_response('mlb/index.html', 
		{'players': players, 
		'homeRunLeaders': homeRunLeaders})
		
def player(request, playerID):
	
	try:
		p = Player.objects.get(pk=playerID)
		seasons = PlayerBatting.objects.filter(Player=playerID).order_by('Year')
		
	except Player.DoesNotExist:
		raise Http404
	
	return render_to_response('mlb/player.html', 
		{'player': p,
		'seasons': seasons})
	