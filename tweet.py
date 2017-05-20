import tweepy
import json

class Tweets:
	ckey = 'bfPWLzqBxtneLRRjYKO7YxcmE'
	csecret = 'F2XAxjwJSe92d34HnIpSiRiHaDaGZmY5pDoVwNM5Ln3jWXxQTb'
	atoken = '865191702054674434-SlJifqwHAgezJUmK1FtpjmbAv4dV48A'
	asecret = 'ExATx9ybQu6AU0hwTmnv80MlHL5c4Rs8HDCWCmmB0fvmn'

	def getRetweets(self):
		tweet_list = []
		auth = tweepy.OAuthHandler(self.ckey, self.csecret)
		auth.set_access_token(self.atoken, self.asecret)

		api = tweepy.API(auth)

		stuff = api.user_timeline(screen_name = 'kayako', count = 20000)

		for status in stuff:
			if (status._json['retweet_count'] >= 1 and "#custserv" in status._json['text']):
				data = {}
				data['text'] = status._json['text']
				tweet_list.append(data)

		return tweet_list