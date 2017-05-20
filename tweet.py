import tweepy
import json
import config

class Tweets:
	
	#accessing the authorisation tokens from config.py
	ckey = config.auth['ckey']
	csecret = config.auth['csecret']
	atoken = config.auth['atoken']
	asecret = config.auth['asecret']

	#method defined to extract the tweets
	def getTweets(self):

		tweet_list = []
		
		auth = tweepy.OAuthHandler(Tweets.ckey, Tweets.csecret)
		auth.set_access_token(Tweets.atoken, Tweets.asecret)
		api = tweepy.API(auth)
		
		#results contain all the tweets by kayako
		results = api.user_timeline(screen_name = 'kayako', count = 17000)

		#iterating through all the tweets
		for result in results:
			if (result._json['retweet_count'] >= 1 and "#custserv" in result._json['text']): #checking for the two conditions
				data = {}
				data['text'] = result._json['text']

				#appending only the approved tweets to a list
				tweet_list.append(data)

		return tweet_list