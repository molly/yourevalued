#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Molly White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tweepy
from secrets import *
from random import choice

queries = ['"nobody likes me"',
           '"nobody loves me"']

filters = ['http',
           '#nowplaying',
           'youtube',
           '-',
           '"',
           '“',
           '”']

def get_tweet():
    '''Get a list of tweets matching the search query.'''
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    query = choice(queries)
    results = api.search(q=query)
    return results

def filter_tweets(tweets):
    '''Filter out tweets to avoid things like song lyrics, etc.'''
    while True:
        tweet = tweets.pop(0)
        text = tweet.text
        if any(substr in text for substr in filters):
            print("filtered: " + text)
        else:
            print(text)
        if len(tweets) == 0:
            break

def send_reply(tweet):
    print(tweet)


if __name__ == "__main__":
    tweets = get_tweet()
    tweet = filter_tweets(tweets)
    send_reply(tweet)