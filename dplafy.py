#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, bitly_api

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

dpla_data = "http://api.dp.la/v2/items?q=motorcycle+OR+harley+OR+fries+OR+hamburger+OR+hotdog+eagle+OR+flag+OR+beer+OR+beef+OR+war+OR+cow+OR+explosion+OR+explosive+OR+gun+OR+chrome&page_size=500&api_key=SOMETHING"

response = urllib.urlopen(dpla_data);
data = json.loads(response.read())
docs = data["docs"]

items = random.sample(docs,1)

for item in items:
  url = item["isShownAt"]
  description = item["sourceResource"]["title"]
  fuck_yeah = "#muricafuckyeah"
  description = description + "\n" + fuck_yeah
  if len(description) > 103:
    while len(description) + 3 > 102:
      description = description[:len(description) - 1]
    description = description + '...'
  tweet_text = "%s %s" % (description,url)
  api.update_status(tweet_text)
