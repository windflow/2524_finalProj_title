#!/usr/bin/env python
#It helps you look for any flying tweets containing keywords that you are interested
#User can choose from two features: (sample)showing currently flying tons of tweets OR (filter) only showing tweets including fun keywords user entered
#Author: Muzi Ti


import time
from getpass import getpass  #for future use
from textwrap import TextWrapper #it might not be used for now
from tweepy import OAuthHandler
import tweepy


 # Prompt for login credentials and setup stream object



#build a twitter listener
class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print self.status_wrapper.fill(status.text) #some format
            print '\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source)
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, error_code):
        print 'An error has occured! Status code = %s' % error_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Zzz Zzz'


def main():
    APP_KEY = "wFxNauOh69Yrkmx8yAC2JjnyF"
    APP_SECRET = "f6TVCedS3Ia7NZURGifAQi9PHTJwIUYGYsZUJqRv4iSLuYgV4E"
    OAUTH_TOKEN = "805290312-k8Mpf4kDpfAHDrtzEj4w2KBPdHxSdP2gCMAnwN8W"
    OAUTH_TOKEN_SECRET = "5nKd38GBF7tVMGiYKugrTu3K92FqvU5Q0UlPLYW2ChMai"
    auth = OAuthHandler(APP_KEY, APP_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream = tweepy.Stream(auth, StreamWatcherListener(), timeout=None)
    # Prompt for mode of streaming
    valid_modes = ['sample', 'filter']
    while True:
        mode = raw_input('Mode? choose one [sample/filter] ') #let user choose what to do
        if mode in valid_modes:
            break
        print 'Invalid mode! Try again.'

    if mode == 'sample':
        stream.sample()

    elif mode == 'filter':
        keyword_list = raw_input('keyword to track ').strip() #get keyword from user
        #track_list = raw_input('Keywords to track (comma seperated): ').strip()


        print "u r searching %s" % keyword_list
        stream.filter(track=keyword_list) #track conditions


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'
