#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014–2016 Molly White
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
import random
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

tweets = [
  "Please ask for help if you need it.\n\nNational Suicide Prevention Lifeline: 1-800-273-8255",
  "National Suicide Prevention Lifeline: 1-800-273-8255\n\nCrisis Text Line: Text START to 741-741\n\nInternational Support: http://www.suicide.org/international-suicide-hotlines.html",
  "If you or someone you know needs help, or just needs to talk, please call the National Suicide Prevention Lifeline at 1-800-273-8255",
  "If you or someone you know is thinking about suicide, or dealing with a suicide loss, call the National Suicide Prevention Lifeline at 1-800-273-8255"
]

if __name__ == "__main__":
    """Tweet one of several suicide hotline messages."""
    if random.randint(0, 5) == 0:
      auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
      auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
      api = tweepy.API(auth)

      api.update_status(random.choice(tweets))
