import http.client
import os
import json
from pprint import pprint

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '[TOKEN]' }
connection.request('GET', '/v2/competitions/PL/standings', None, headers)
response = json.loads(connection.getresponse().read().decode())

clear()

k = 0

while k < 20:
	pprint(str(k + 1) + " " + response['standings'][0]["table"][k]["team"]["name"])
	k += 1