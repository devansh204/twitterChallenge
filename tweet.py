import tweepy
import json
import config

class Tweets:
	ckey = config.auth['ckey']
	csecret = config.auth['csecret']
	atoken = config.auth['atoken']
	asecret = config.auth['asecret']

	def getRetweets(self):
		tweet_list = []
		auth = tweepy.OAuthHandler(self.ckey, self.csecret)
		auth.set_access_token(self.atoken, self.asecret)

		api = tweepy.API(auth)
		results = api.user_timeline(screen_name = 'kayako', count = 20)

		for result in results:
			if (result._json['retweet_count'] >= 1 and "#custserv" in result._json['text']):
				data = {}
				data['text'] = result._json['text']
				tweet_list.append(data)

		return tweet_list