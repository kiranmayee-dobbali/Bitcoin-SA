#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:51:09 2018

@author: kiranmayee
"""


import sys
import os
import jsonpickle
import tweepy

if __name__ == '__main__':


    ACCESS_TOKEN="2343565507-n7VYZZJ60JwiDEiMohvAHC02YwYVWWB2E7voKRY"
    ACCESS_TOKEN_SECRET="mpAcB0FzpurxBi7anReiMZmJvd40tMvyNNMeNZ5buGpMU"
    CONSUMER_KEY="dpcRBwKBAdBvgsj9matEI8gCV"
    CONSUMER_SECRET="FsGAryx6bF9jqgfHwnfQBwC0Lzuun4NuG71fbj9kgCEoq7lAZy"

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET )
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET )
    api = tweepy.API(auth)
    if (not api):
        print ("Problem connecting to API")
    
    auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET )

#Setting up new api wrapper, using authentication only
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
 
#Error handling
    if (not api):
        print ("Problem Connecting to API")
    
    searchQuery = '#bitcoin OR #BTS'    
#Maximum number of tweets we want to collect 
    maxTweets = 1000000

#The twitter Search API allows up to 100 tweets per query
    tweetsPerQry = 100
    tweetCount = 0

#Open a text file to save the tweets to
    with open('data_historic.json', 'w') as f:

    #Tell the Cursor method that we want to use the Search API (api.search)
    #Also tell Cursor our query, and the maximum number of tweets to return
        for tweet in tweepy.Cursor(api.search,q=searchQuery).items(maxTweets) :         

            #Verify the tweet has place info before writing (It should, if it got past our place filter)
            if tweet.place is not None:
            
            #Write the JSON format to the text file, and add one to the number of tweets we've collected
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                tweetCount += 1

    #Display how many tweets we have collected
    print("Downloaded {0} tweets".format(tweetCount))