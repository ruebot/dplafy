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

dpla_data = "http://api.dp.la/v2/items?q=%22donald+trump%22+OR+motorcycle+OR+%22harley+davidson%22+OR+%22chicken+wings%22+ORturkey+OR+fries+OR+hamburger+OR+hotdog+OR+eagle+OR+%22american+flag%22+OR+beer+OR+beef+OR+war+OR+cow+OR+explosion+OR+explosive+OR+gun+OR+chrome&page_size=500&api_key=91b1bb54a822c576aa55d1b7a9babbd6"

response = urllib.urlopen(dpla_data);
data = json.loads(response.read())
docs = data["docs"]

items = random.sample(docs,1)

for item in items:
  url = "https://dp.la/item/" + item["id"]
  description = item["sourceResource"]["title"][0]
  fuck_yeah = "#muricafuckyeah"
  description = (description[:102] + '...') if len(description) > 102 else description
  if len(description) <= 1:
      break
  us_flag = u'\U0001F1FA\U0001F1F8'
  description = description + "\n" + " " + us_flag + " " + fuck_yeah
  tweet_text = "%s %s" % (description,url)
  api.update_status(tweet_text)
