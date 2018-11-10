import json
import os

def searchJSON():
	lst = []

	for line in open('./api/current_cities.json', 'r'):      # opens json file and iterates through every line
	    x = json.loads(line)                                            # converts line into list
	    lst.append((x['name'], x['_id']))                 # appends city, country, and city id to lst

	return lst