import sys
import requests
import geocoder
import pywapi 
import json

def noaa(zipcode):
	location = geocoder.google(zipcode)
	lookup = pywapi.get_location_ids(location.city + ',' + location.state)
	key = lookup.keys()
	optimalWeather = list()
	weather_result = pywapi.get_weather_from_weather_com(key[0])
	for x in range(0, len(weather_result['forecasts'])):
		print(weather_result['forecasts'][x]['date'] + ': ' +
		weather_result['forecasts'][x]['night']['brief_text'])
		if 'Clear' in weather_result['forecasts'][x]['night']['brief_text']:
			optimalWeather.append(weather_result['forecasts'][x]['date'])
	print optimalWeather
