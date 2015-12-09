###2524 final project
#using smtp here instead of twilio
#twilio usr:timuzi2011@gmail.com; pw: Tmz#19901025 twilio cell: (1)5405851302
#tweepy: #Set Twitter application authentication
#	APP_KEY = "wFxNauOh69Yrkmx8yAC2JjnyF"
#	APP_SECRET = "f6TVCedS3Ia7NZURGifAQi9PHTJwIUYGYsZUJqRv4iSLuYgV4E"
#	OAUTH_TOKEN = "805290312-k8Mpf4kDpfAHDrtzEj4w2KBPdHxSdP2gCMAnwN8W"#
#	OAUTH_TOKEN_SECRET = "5nKd38GBF7tVMGiYKugrTu3K92FqvU5Q0UlPLYW2ChMai"
#	auth = OAuthHandler(APP_KEY, APP_SECRET)
#	auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#



import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import Twitter, OAuth, TwitterStream,TwitterHTTPError
from tweepy.streaming import StreamListener
try:
    import json
except ImportError:
    import simplejson as json
import smtplib

#Set up twitter API identification
#"token": you can follow twitter official doc to get it and remember to change the perm as read/write
APP_KEY = "wFxNauOh69Yrkmx8yAC2JjnyF"
APP_SECRET = "f6TVCedS3Ia7NZURGifAQi9PHTJwIUYGYsZUJqRv4iSLuYgV4E"
OAUTH_TOKEN = "805290312-k8Mpf4kDpfAHDrtzEj4w2KBPdHxSdP2gCMAnwN8W"
OAUTH_TOKEN_SECRET = "5nKd38GBF7tVMGiYKugrTu3K92FqvU5Q0UlPLYW2ChMai"
auth = OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


'''
#init connecttion
#auth doesn't work
#twitter_stream = TwitterStream(auth=auth)
#get flowing tweets
tweets_data = TwitterStream.status.sample()

#keep collecting tweets until we get 50
tweet_count = 100

print "connected!"

for tweet in tweets_data:
    tweet_count -= 1
    print json.dumps(tweet)

    if tweet_count <= 0:
        break
'''



username = "timuzi2011@hotmail.com" #txt sent from
password = "tmz19901025"

atttext = "5409980101@txt.att.net" # user cell no. that you send to + @*** at&t gateway// @vtext.com --verizon gate way
message = "A new super important tweet Event!"

msg = """From: %s
To: %s
Subject: text-message
%s""" % (username, atttext, message)

server = smtplib.SMTP('smtp.live.com',587) #server
server.starttls()#start tls
server.login(username,password)


#streamListener to be collecting tweets that we want
class my_listener(StreamListener):
    def on_data(self, data):
        print"Collecting data"
        print(data)
        server.sendmail(username, atttext, msg)#finally send txt
        print "A text msg of notification should be sent"
        return(True)

    def on_error(self, status):
        print status


twitterStream = Stream(auth, my_listener())
twitterStream.filter(track=["@TiMuzi"]) #colllecting any data @ to specific user(or any keywords like "car")
