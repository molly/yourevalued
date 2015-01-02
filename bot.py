#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014–2015 Molly White
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
import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
tweeted_file = os.path.join(__location__, "tweeted_users.txt")

data = {'like':
            {'queries': ['"nobody likes me"',
                         '"nobody loves me"'],
             'responses': ['I like you.',
                           'You\'re valued.',
                           'You matter.',
                           u'\u2764']
            }
        }

filters = ['http',
           '#nowplaying',
           'youtube',
           '-',
           '"',
           u'“',
           u'”',
           'poor boy',
           'the way you do',
           'hear it every day',
           'but that\'s ok',
           'but thats ok']


def get_tweet(api_, type_):
    """Get a list of tweets matching the search query."""
    query = choice(data[type_]['queries'])
    results = api_.search(q=query, count=50)
    return results


def get_users():
    """Get a list of users we've already tweeted at."""
    f = open(tweeted_file, 'r')
    usrs = [line.rstrip('\n') for line in f]
    return usrs


def filter_tweets(tweets_, users_):
    """Filter out tweets to avoid things like song lyrics, etc."""
    while True:
        tweet_ = tweets_.pop(0)
        text = tweet_.text
        if len(tweets) == 0:
            return
        if not (hasattr(tweet_, "retweeted_status") or
                tweet_.in_reply_to_status_id or
                tweet_.author.screen_name in users_ or
                any(substr in text.lower() for substr in filters)):
            return tweet_


def send_reply(api_, type_, tweet_):
    """Send the reply tweet and record it."""
    f = open(tweeted_file, 'a')
    f.write(tweet_.author.screen_name + '\n')
    f.close()
    text = '@' + tweet_.author.screen_name + ' ' + choice(data[type_]['responses'])
    api_.update_status(text, in_reply_to_status_id=tweet_.id_str)


if __name__ == "__main__":
    """Find a tweet and reply to it."""
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweet_type = choice(data.keys())

    tweets = get_tweet(api, tweet_type)
    users = get_users()
    tweet = filter_tweets(tweets, users)
    send_reply(api, tweet_type, tweet)
