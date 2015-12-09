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


'''
#send tweet without logging on twitter
#import tweepy

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
'''

from textwrap import TextWrapper
from tweepy import OAuthHandler
import tweepy


class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print self.status_wrapper.fill(status.text)
            print '\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source)
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, error_code):
        print 'An error has occured! Error code = %s' % error_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Zzzzzz'


def main():
    # Prompt for login credentials and setup stream object
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
        mode = raw_input('Mode? [sample/filter] ')
        if mode in valid_modes:
            break
        print 'Invalid mode! Try again.'

    if mode == 'sample':
        stream.sample()

    elif mode == 'filter':
        follow_list = raw_input('Users to follow (comma separated): ').strip()
        track_list = raw_input('Keywords to track (comma seperated): ').strip()
        if follow_list:
            follow_list = [u for u in follow_list.split(',')]
            userid_list = []
            username_list = []

            for user in follow_list:
                if user.isdigit():
                    userid_list.append(user)
                else:
                    username_list.append(user)

            for username in username_list:
                user = tweepy.API().get_user(username)
                userid_list.append(user.id)

            follow_list = userid_list
        else:
            follow_list = None
        if track_list:
            track_list = [k for k in track_list.split(',')]
        else:
            track_list = None
        print follow_list
        stream.filter(follow_list, track_list)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'
