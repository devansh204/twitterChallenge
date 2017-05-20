<b>tweet.py</b>

This file contains the implimentation of <b>Tweepy</b> - a Python wrapper for the Twitter API. The class Tweets in this file contains the method which - connects to the Twitter API, filters the tweets and returns the desired tweets.

<b>config.py</b>

This file contains the authorisation tokens (Access Token, Access Token Secret, Consumer Key, Consumer Secret), which is used in the class defined in tweet.py.

<b>route.py</b>

I have used the <b>Flask</b> - a micro web framework - to create the APIs. For the requests routed to /getTweets, the code returns the list of tweets. 

To Run:
  1) Define the authorisation tokens in config.py
  2) Execute the route.py
  
     ```
     python route.py
     ```
  3) Test the Restful API defined ( default - http://127.0.0.1:5000/getTweets )
