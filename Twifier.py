###2524 final project
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

#Set up twitter API identification
#"token": you can follow twitter official doc to get it and remember to change the perm as read/write
APP_KEY = "wFxNauOh69Yrkmx8yAC2JjnyF"
APP_SECRET = "f6TVCedS3Ia7NZURGifAQi9PHTJwIUYGYsZUJqRv4iSLuYgV4E"
OAUTH_TOKEN = "805290312-k8Mpf4kDpfAHDrtzEj4w2KBPdHxSdP2gCMAnwN8W"
OAUTH_TOKEN_SECRET = "5nKd38GBF7tVMGiYKugrTu3K92FqvU5Q0UlPLYW2ChMai"
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
#update a tweet on under your account(twitter account needed ofc)
api.update_status(status="This is a tweet test sent automatically")
print "Tweet sent, check it online!"

