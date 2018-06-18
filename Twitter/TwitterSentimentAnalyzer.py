import tweepy
from textblob import TextBlob

#This application is meant to collect tweets and gather data
#to be analyzed fo further use

#My twitter apps API
consumer_key = "ldixugoeJP4Mbsj3t2FovQF4x"
consumer_secret = "85Ew7cyokcHcyOiOB7oCj7YTfANpHWOt6osdHK0t1NUPpBN1kR"

#This access token can be used to make API requests on your own account's behalf.
access_token = "996752375770644482-XJgGbNwyx5UbwrStQoNh9bzqV9NtUT3"
access_token_secret = "vHSeJ6x5lPccqF3HXsZ1dMCkduaC2hl89PY3naJBlZKfB"

#Authentication handler for logging in
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#this variable will make us able to
#Create tweets
#Delete tweets
#Find other users
api = tweepy.API(auth)

#variable to store public tweets using the .search method
#the search method only takes a single argument that we will search for
public_tweets = api.search('Trump')

#Let's create a file to store our data in
#first we assign the name om the file followed by a 'w+'
#the w stands for write while + stands for creating the file
#if it doesn't already exist
file = open("tweets.txt", "w+")
file2 = open("analysis.txt", "w+")

for tweet in public_tweets:
    file.write(tweet.text)
    analysis = TextBlob(tweet.text)
    file2.write(str(analysis))
