#!/usr/bin/python
# -*- coding: utf-8 -*-

import twitter, json, datetime, time
CONSUMER_KEY = 'BcL5Jj9DMxkaXE3ngxV2Cu38n'
CONSUMER_SECRET = '8gjdx6ucRK01KqcegmwQrUuBXct1gkfRWGAukNDorhSUDMLRa0'
OAUTH_TOKEN = '124769940-B62NVTfGOupNhWUC4aKmgOhKFzTOqJWCzc6hmHwu'
OAUTH_TOKEN_SECRET = 'KvpnnEZfZATMGIVoRgtXl9xZsLqJLvckk04IdCnRLyN90'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
trends_av = twitter_api.trends.available()
for i in range(len(trends_av)):
	if trends_av[i]['name'] == 'Korea':
		KOR_WOE_ID = trends_av[i]['woeid']

WORLD_WOE_ID = 1
US_WOE_ID = 23424977


def writeTrends(trend, f):
	trend = json.loads(json.dumps(trend))
	trend_list = trend[0]['trends']
	trend_name = []

	with open(f, "a") as myfile:
		myfile.write(trend[0]['as_of'] + '\n')
		myfile.write(trend[0]['locations'][0]['name'] + '\n')
		print trend[0]['as_of']
		print trend[0]['locations'][0]['name']
	
		for i in range(len(trend_list)):
			trend_name.append(trend_list[i]['name'])
			print trend_name[i].encode('utf-8')
			try:
				myfile.write(trend_name[i].encode('utf-8') + '\n')
			except UnicodeEncodeError, e:
				print 'Encoding Error' + trend_name[i] + '\n'
		myfile.close()

def getTrends():
	kor_trends = twitter_api.trends.place(_id = KOR_WOE_ID)
	us_trends = twitter_api.trends.place(_id = US_WOE_ID)
	world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)
	return kor_trends, us_trends, world_trends

us = file('us_trends.txt', 'a')
kor = file('kor_trends.txt', 'a')
world = file('world_trends.txt', 'a')

def checkCurrentTime():
	now = datetime.datetime.now()
	if now.minute == 0:
		kor_trends, us_trends, world_trends = getTrends()
		writeTrends(kor_trends, 'kor_trends.txt')
		writeTrends(us_trends, 'us_trends.txt')
		writeTrends(world_trends, 'world_trends.txt')
	elif now.minute == 30:
		kor_trends, us_trends, world_trends = getTrends()
		writeTrends(kor_trends, 'kor_trends.txt')
		writeTrends(us_trends, 'us_trends.txt')
		writeTrends(world_trends, 'world_trends.txt')
	elif now.minute == 15:
		kor_trends, us_trends, world_trends = getTrends()
		writeTrends(kor_trends, 'kor_trends.txt')
		writeTrends(us_trends, 'us_trends.txt')
		writeTrends(world_trends, 'world_trends.txt')
	elif now.minute == 45:
		kor_trends, us_trends, world_trends = getTrends()
		writeTrends(kor_trends, 'kor_trends.txt')
		writeTrends(us_trends, 'us_trends.txt')
		writeTrends(world_trends, 'world_trends.txt')

while True:
	time.sleep(30)
	checkCurrentTime()
	print "Loading", datetime.datetime.now()
	

