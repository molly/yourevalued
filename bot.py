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

data = {
    'like': {
        'queries': ['"nobody likes me"',
                    '"nobody loves me"'],
        'responses': ['I like you.',
                      'You\'re valued.',
                      u'\u2764']
    }
}

filters = ['http',
           '#nowplaying',
           'youtube',
           '-',
           '"',
           u'“',
           u'”']

def get_tweet(api, type):
    '''Get a list of tweets matching the search query.'''
    query = choice(data[type]['queries'])
    results = api.search(q=query, count=50)
    return results

def get_users():
    '''Get a list of users we've already tweeted at.'''
    f = open('tweeted_users.txt', 'r')
    users = [line.rstrip('\n') for line in f]
    return users

def filter_tweets(tweets, users):
    '''Filter out tweets to avoid things like song lyrics, etc.'''
    page = 1
    while True:
        tweet = tweets.pop(0)
        text = tweet.text
        if not (any(substr in text for substr in filters) or tweet.author.screen_name in users):
            return tweet
        if len(tweets) == 0:
            return

def send_reply(api, type, tweet):
    text = '@' + tweet.author.screen_name + ' ' + choice(data[type]['responses'])
    print(text)
    #api.update_status(text, in_reply_to_status_id = tweet.id_str)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    type = choice(data.keys())

    tweets = get_tweet(api, type)
    users = get_users()
    tweet = filter_tweets(tweets, users)
    send_reply(api, type, tweet)