from __future__ import division
from models import Player, PlayerBattingSeason, PlayerBattingCareer, PlayerBattingCareerPercentile
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import HttpResponse, Http404
import json

def getLeaderCareerYears(fieldAbbrev):
	
	thisField = PlayerBattingCareer.fieldLookup('abbrev', fieldAbbrev)
	leaders = getLeaderCareers(fieldAbbrev)
	
	if leaders != False:
		leaderCareers = []
		leaderIDs = []
		
		for leader in leaders:
			playerID = leader.Player.PlayerID
		
			if playerID not in leaderIDs:
				leaderCareer = leader.Player.getCareerStats(thisField['fieldName'], True)
				leaderCareers.append(leaderCareer)
				leaderIDs.append(playerID)
		
		return leaders, leaderCareers
	else:
		return False, False

def getLeaderCareers(fieldAbbrev):
	thisField = PlayerBattingCareer.fieldLookup('abbrev', fieldAbbrev)
	if thisField != False:
		leaders = PlayerBattingCareer.objects.order_by('-' + thisField['fieldName'])[:30]
		return leaders
	else:
		return False

def makeLeaderStatsRows(leaders):
	leaderStatsRows = []
	leaderNames = []
	for leader in leaders:
		leaderNames.append('<a href="/mlb/player/' + leader.Player.PlayerID + '/">' + str(leader) + '</a>')
	
	i=0
	for leader in leaders.values():
		leaderStatsRow = []
		leaderStatsRow.append(leaderNames[i])
		for field in PlayerBattingCareer.FIELDS:
			if field['fieldName'] != 'Player' and field['fieldName'] != 'GamesBatting':
				leaderStatsRow.append(leader[field['fieldName']])
		leaderStatsRows.append(leaderStatsRow)
		i+=1
	
	return leaderStatsRows

def makeLeaderPercentileRows(leaders):
	PER_AB_FIELDNAMES = [
        'Runs', 'Hits', 'Doubles', 'Triples', 'Homeruns','RunsBattedIn', 'StolenBases', 'CaughtStealing',
        'BaseOnBalls', 'Strikeouts', 'IntentionalWalks', 'HitByPitch', 'SacrificeHits', 'SacrificeFlies',
        'GroundedIntoDouble'
    ]

	pTiles = PlayerBattingCareerPercentile.objects.order_by('-Percentile').values()
	leaderDicts = leaders.values()
	leaderPTileDict = {}
	
	for leader in leaderDicts:
		atBats = leader['AtBats']
		for fieldName in PER_AB_FIELDNAMES:
			leader[fieldName] = float(leader[fieldName]) / float(atBats)
	
	for field in PlayerBattingCareer.FIELDS:
		fieldName = field['fieldName']
		if fieldName != 'Player' and fieldName != 'GamesBatting':
			
			sortedLeaders = sorted(leaderDicts, key=lambda k: k[fieldName], reverse=True)
			pTileIndex = 0
		
			for thisPlayer in sortedLeaders:
				statValue = thisPlayer[fieldName]
				playerID = thisPlayer['Player_id']
			
				if playerID not in leaderPTileDict:
					leaderPTileDict[playerID] = []
			
				while(pTiles[pTileIndex+1][fieldName] > statValue):
					pTileIndex += 1
					if pTileIndex >= len(pTiles):
						break
			
				thisPTile = pTiles[pTileIndex]['Percentile']
				leaderPTileDict[playerID].append(thisPTile)
	
	leaderPTileRows = []
	for leader in leaderDicts:
		leaderPTiles = leaderPTileDict[leader['Player_id']]
		leaderPTiles.insert(0, None)
		leaderPTileRows.append(leaderPTiles)
	
	return leaderPTileRows

def combineStatsAndPTiles(stats, pTiles):
	statsAndPTiles = []
	for i in range(0, len(stats)):
		thisRow = []
		for j in range(0, len(stats[i])):
			thisStat = {}
			thisStat['stat'] = stats[i][j]
			if i < len(pTiles) and j < len(pTiles[i]):
				thisStat['pTile'] = pTiles[i][j]
			else:
				thisStat['pTile'] = None
			thisRow.append(thisStat)
		
		statsAndPTiles.append(thisRow)
	return statsAndPTiles

def index(request):
	leaders, leaderCareers = getLeaderCareerYears('HR')
	
	leaderCareersJSON = json.dumps(leaderCareers)
	
	leaderStatsRows = makeLeaderStatsRows(leaders)
	leaderPTileRows = makeLeaderPercentileRows(leaders)
	
	leaderStatsAndPTiles = combineStatsAndPTiles(leaderStatsRows, leaderPTileRows)
	
	return render_to_response('mlb/index.html', 
		{'playerBattingCareerFields': PlayerBattingCareer.FIELDS,
		'homeRunLeaders': leaders,
		'leaderCareersJSON': leaderCareersJSON,
		'leaderStatsRows': leaderStatsRows,
		'leaderPTileRows': leaderPTileRows,
		'leaderStatsAndPTiles': leaderStatsAndPTiles})

def leaderApi(request, fieldAbbrev):
	
	leaders, leaderCareers = getLeaderCareerYears(fieldAbbrev)
	
	if leaders != False:
		#leadersJSON = serializers.serialize('json', leaders, ensure_ascii=False)
		leaderCareersJSON = json.dumps(leaderCareers)
		#leaderCareerStatsJSON = '{"leaders": '+leadersJSON+', "leaderCareers":'+leaderCareersJSON+'}'
		
		return HttpResponse(leaderCareersJSON)
	
	else:
		raise Http404

def leaderTableApi(request, fieldAbbrev):
	leaderCareers = getLeaderCareers(fieldAbbrev)
	
	leaderStatsRows = makeLeaderStatsRows(leaderCareers)
	leaderPTileRows = makeLeaderPercentileRows(leaderCareers)
	
	leaderStatsAndPTiles = combineStatsAndPTiles(leaderStatsRows, leaderPTileRows)
	
	return render_to_response('mlb/table.html', 
		{'playerBattingCareerFields': PlayerBattingCareer.FIELDS,
		'leaderStatsRows':leaderStatsRows,
		'leaderStatsAndPTiles': leaderStatsAndPTiles})

def player(request, playerID):
	
	try:
		p = Player.objects.get(pk=playerID)
		seasons = PlayerBattingSeason.objects.filter(Player=playerID).order_by('Year')
		
	except Player.DoesNotExist:
		raise Http404
	
	return render_to_response('mlb/player.html', 
		{'player': p,
		'seasons': seasons})
	