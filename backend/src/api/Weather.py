import datetime
import requests
import json
import re

# formats unixtime to (Hour:Minute AM/PM)
def time_converter(time):
	formatted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
	return formatted_time

# gathers raw data from server (json)
def data_fetch(city_str, user_api):
	if ',' in city_str:
		city, country = city_str.split(',')
		country_list = re.split("(%20+)", country)
		for i in range(len(country_list)):
			if country_list[i].isspace():
				country_list[i] = "+"
		country = ''.join(country_list)

		city_list = re.split("(%20+)", city)
		for i in range(len(city_list)):
			if city_list[i].isspace():
				city_list[i] = "+"
		city = ''.join(city_list) + ',' + country

	else:
		city_list = re.split("(%20+)", city_str)
		for i in range(len(city_list)):
			if city_list[i].isspace():
				city_list[i] = "+"
		city = ''.join(city_list)

	results = requests.get("http://api.openweathermap.org/data/2.5/weather",
							params={'q': city, 'units': 'metric', 'appid': user_api})
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
def data_organizer(response):
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

	return temp

def main(city):
	user_api = "70541da258ef9821825fb78ffd153f7a"	# insert api key from OpenWeatherMap here
	return data_organizer(data_fetch(city, user_api))