import tweet
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Server Working'

@app.route('/getTweets')
def returnTweets():
	tweet_list = tweet.functionname()
	return jsonify(results=tweet_list)

if __name__ == '__main__':
   app.run("127.0.0.1", "5009")