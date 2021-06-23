# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:49:38 2021

@author: gargt
"""

import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

fh=open('WeatherData.txt','w')

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")

print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

fh.write("-------------------------------------------------------------")
fh.write("\n")
fh.write(location)
fh.write("\n")
fh.write(date_time)
fh.write("\n")
fh.write(str(temp_city))
fh.write("\n")
fh.write(weather_desc)
fh.write("\n")
fh.write(str(hmdt))
fh.write("\n")
fh.write(str(wind_spd))
fh.write("\n")
fh.write("--------------------------------------------------------------")


