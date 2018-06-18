import tweepy
from textblob import TextBlob

#This application is meant to collect tweets and gather data
#to be analyzed fo further use
#https://apps.twitter.com/app/

#My twitter apps API
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"

#This access token can be used to make API requests on your own account's behalf.
access_token = "access_token"
access_token_secret = "access_token_secret"

#Authentication handler for logging in
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#this variable will make us able to
#Create tweets
#Delete tweets
#Find other users
api = tweepy.API(auth)


#variables for dates from when i will be stripping data
person_of_interest = '@realDonaldTrump'
since_date = "01-01-2016"
until_date = "19-06-2018"

#variable to store public tweets using the .search method
#the search method only takes a single argument that we will search for
public_tweets = api.search(q = person_of_interest, count = 1000, since = since_date, until = until_date)


#Let's create a file to store our data in
#first we assign the name om the file followed by a 'w+'
#the w stands for write while + stands for creating the file
#if it doesn't already exist
file = open("tweets.txt", "a+")


for tweet in public_tweets:
    file.write(tweet.text)
    analysis = TextBlob(tweet.text)
    file.write(str(analysis))
