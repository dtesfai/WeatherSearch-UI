import datetime
import urllib
import requests
import json
import os
from .fileSearcher import search

# formats unixtime to (Hour:Minute AM/PM)
def time_converter(time):
	formatted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
	return formatted_time

# gathers raw data from server (json)
def data_fetch(city_id, user_api):
	results = requests.get("http://api.openweathermap.org/data/2.5/weather",
							params={'id': city_id, 'appid': user_api})
	return results

# formats direction at which wind is travelling
def degree_formatter(degrees):
	unit_symbol = '\u00b0'
	axis = {0:'N', 90:'E', 180:'S', 270:'W'}
	if (degrees in axis):
		output = '[{}]'.format(axis[degrees])
	else:
		v_diff = 'S' if (180 - degrees) < degrees else 'N'
		h_diff = 'E' if (90 - degrees) < (270 - degrees) else 'W'
		degrees = min(abs(degrees - 90), abs(90 - degrees), abs(degrees - 180), abs(180 - degrees), abs(degrees - 270), abs(270 - degrees))
		output = '[{} {}{} {}]'.format(v_diff, round(degrees, 2), unit_symbol, h_diff)
	return output

# creates dictionary that organizes important information from raw data  
def data_organizer(response, data):
	formatted_response = json.loads(response.text)

	name = formatted_response['name']
	country = formatted_response['sys']['country']

	temp = {
		"name" : name,
		"country" : country,
		"condit" : formatted_response['weather'][0]['main'],
		"temp" : formatted_response['main']['temp'],
		"temp_min" : formatted_response['main']['temp_min'],
		"temp_max" : formatted_response['main']['temp_max'],
		"humidity" : formatted_response['main']['humidity'],
		"wind_speed" : formatted_response['wind']['speed'],
		"wind_deg" : degree_formatter(formatted_response['wind']['deg']),
		"sunrise" : time_converter(formatted_response['sys']['sunrise']),
		"sunset" : time_converter(formatted_response['sys']['sunset']),
		"clouds" : formatted_response['clouds']['all'],
		"time" : time_converter(formatted_response['dt'])
	}

	data[formatted_response['id']] = temp

	return data

def main(city):
	city_list = search(city)	# methods in fileSearcher module determine which city to find weather of
	user_api = "70541da258ef9821825fb78ffd153f7a"	# insert api key from OpenWeatherMap here

	data = data_fetch(city_list[1][1], user_api)
	return json.loads(data.text)