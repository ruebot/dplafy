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

dpla_data = "http://api.dp.la/v2/items?sourceResource.description=%22chicken+wings%22+OR+fries+OR+hamburger+OR+hotdog+OR+eagle+OR+beer+OR+beef++OR+%22all+you+can+eat%22&page_size=500&api_key=91b1bb54a822c576aa55d1b7a9babbd6"

response = urllib.urlopen(dpla_data);
data = json.loads(response.read())
docs = data["docs"]

items = random.sample(docs,1)

for item in items:
  url = "https://dp.la/item/" + item["id"]
  description = item["sourceResource"]["description"][0]
  description = (description[:102] + '...') if len(description) > 102 else description
  if len(description) <= 1:
      break
  us_flag = u'\U0001F1FA\U0001F1F8'
  hotdog = u'\U0001F32D'
  eagle = u'\U0001F985'
  description = description + "\n" + " " + hotdog + " " + eagle + " " + us_flag
  tweet_text = "%s %s" % (description,url)
  api.update_status(tweet_text)
