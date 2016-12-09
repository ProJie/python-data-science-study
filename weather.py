# coding=utf-8
# 天气接口，city=城市名
# http://wthrcdn.etouch.cn/WeatherApi?city=%E5%8C%97%E4%BA%AC
import codecs

import requests

API = 'http://wthrcdn.etouch.cn/WeatherApi'


def get_weather(city='焦作'):
	wea = requests.get(API, params={'city': city})
	write_xml(wea.text)
	print(wea.text)


def write_xml(data):
	with codecs.open('weather.xml', 'w', encoding='utf-8') as wea_file:
		wea_file.write(data)


get_weather('焦作')
