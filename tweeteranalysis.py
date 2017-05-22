from tweetpy import *
import re
import json

try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 	'757845079977439232-H3fBRlJeSQ9FO2KuegCXACltg7rZ6V4'
ACCESS_SECRET = 'nVpcbAyN7ZAmjZ3zpZFZAyqWRayRgwd207zKYxjzvbc3U'
CONSUMER_KEY = 'b50Z4BqdjF7QgZdBubFvZdE0f'
CONSUMER_SECRET = 'vk875skjomkWJKOZPNVniO6biW8FzVkV6McRUOdj9GwTRFoPLH'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="#kindle",language="en",replies="all")
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10000000

alist=[]
for tweet in iterator:
    tweet_count -= 1
    file = "C:\\Users\\WELCOME\\Desktop\\twitterfeeds.json"
    alist.append(tweet)
    with open(file, 'w+') as outfile:
        for i in alist:
            json.dump(i,outfile)


    #emo = re.findall('^(:\(|:\))+$',tweet)
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print tweet

#        fid.write(tweet)

#    while emo == '':
 #       print emo


#if tweet_count <= 0:
#    break