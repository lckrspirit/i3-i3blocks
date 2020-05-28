#!/bin/python

import os


weather_url = 'curl http://wttr.in/Bishkek\?format\=3 2> /dev/null'


def get_weather(weather):
	if not os.popen(weather).read():
		print(f'Connection error..')
	else:
		print(f'{os.popen(weather).read().strip()}')


get_weather(weather_url)