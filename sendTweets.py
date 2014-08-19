#-------------------------------------------------------------------------------
# Name:        sendTweets
# Purpose:     Send tweets straight from Python.
#
# Author:      Alex Lavin
#
# Created:     19/08/2014
# Copyright:   (c) Alex Lavin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sendTweet(tweet):
    import tweepy
    import json

    # Consumer keys and access tokens, used for OAuth
    consumer_key = 'RE5Dk8JNoNdkyUUaERyXXUjYE'
    consumer_secret = 'aHXgYvBHReg36Uh2634wACveUTlkpfAXES4MlEJavz2w7NrkmL'
    access_token = '858827671-LI5OHZJyQOaavaLahmSMpPrgA0fJFZgVl1aaeRax'
    access_token_secret = 'F8nGZPzLRuIzMiLedZNMHRdEe03amwTVEzj8pF7sRynFa'
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Get API handler
    api = tweepy.API(auth)
    # Tweet...
    if tweet==[]:
        tweet = 'Hello world! It\'s %s' % (time.strftime("%H:%M:%S"))
    print "Tweeting:", tweet
    api.update_status(tweet)

if __name__ == '__main__':
    tweet = 'This tweet is straight out of Python! Check out the code on my Github: https://github.com/BoltzmannBrain'
    sendTweet(tweet)
