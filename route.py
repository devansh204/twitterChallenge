from tweet import Tweets
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Server Working'

@app.route('/getTweets')
def getRetweets():
	t = Tweets()
	tweet_list = t.getRetweets()
	return jsonify(results=tweet_list)

if __name__ == '__main__':
   app.run()