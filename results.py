import http.client
import os
import json
from pprint import pprint

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '[TOKEN]' }

connection.request('GET', '/v2/competitions/PL/matches', None, headers)
response = json.loads(connection.getresponse().read().decode())

team = input("Enter team > ").lower()

k = 1

team_for = 0
team_ag = 0

team_points = 0

while k < 380:
	forgoals = response['matches'][k]['score']['fullTime']['homeTeam']
	againstgoals = response['matches'][k]['score']['fullTime']['awayTeam']
	if response['matches'][k]['homeTeam']['name'].lower() == team + " fc":
		if forgoals != None:
			print(response['matches'][k]['homeTeam']['name'] + " " + str(forgoals) + " - " + str(againstgoals) + " " + response['matches'][k]['awayTeam']['name'])
			team_for += forgoals
			team_ag += againstgoals
			if forgoals > againstgoals:
				team_points += 3
			elif forgoals == againstgoals:
				team_points += 1
	forgoals = response['matches'][k]['score']['fullTime']['awayTeam']
	againstgoals = response['matches'][k]['score']['fullTime']['homeTeam']
	if response['matches'][k]['awayTeam']['name'].lower() == team + " fc":
		if forgoals != None:
			print(response['matches'][k]['homeTeam']['name'] + " " + str(againstgoals) + " - " + str(forgoals) + " " + response['matches'][k]['awayTeam']['name'])
			team_for += forgoals
			team_ag += againstgoals
			if forgoals > againstgoals:
				team_points += 3
			elif forgoals == againstgoals:
				team_points += 1
	k = k + 1

k = 1

print("Points: " + str(team_points))
print("For: " + str(team_for))
print("Against: " + str(team_ag))
