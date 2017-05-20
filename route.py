from tweet import Tweets
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def check():
   return 'Server Working'

#defining the API here
@app.route('/getTweets')
def getRetweets():

	#create an instance of Tweets class
	t = Tweets()
	tweet_list = t.getTweets()

	#return the list of tweets
	return jsonify(results=tweet_list)

if __name__ == '__main__':
   app.run()