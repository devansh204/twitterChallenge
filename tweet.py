import tweepy
import json

ckey = ''
csecret = ''
atoken = ''
asecret = ''

def functionname():
	tweet_list = []
	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	api = tweepy.API(auth)

	stuff = api.user_timeline(screen_name = 'kayako', count = 20000)

	for status in stuff:
		if (status._json['retweet_count'] >= 1 and "#custserv" in status._json['text']):
			data = {}
			data['text'] = status._json['text']
			tweet_list.append(data)
	return tweet_list