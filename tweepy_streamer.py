#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:15:09 2018

@author: kiranmayee
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 

 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        ACCESS_TOKEN="2343565507-n7VYZZJ60JwiDEiMohvAHC02YwYVWWB2E7voKRY"
        ACCESS_TOKEN_SECRET="mpAcB0FzpurxBi7anReiMZmJvd40tMvyNNMeNZ5buGpMU"
        CONSUMER_KEY="dpcRBwKBAdBvgsj9matEI8gCV"
        CONSUMER_SECRET="FsGAryx6bF9jqgfHwnfQBwC0Lzuun4NuG71fbj9kgCEoq7lAZy"
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["#bitcoin", "#BTS"]
    fetched_tweets_filename = "btweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)