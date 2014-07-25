import json
import requests
import tweepy
import time
import os.path

access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_KEY_SECRET_HERE'

def strip_title(title):   #Make sure that the tweet fits within 140 characters
  if len(title) < 114:
    return title
  else:
    return title[:113] + "..."

def tweet_creator(subreddit):
    post_content = []
    post_ids = []
    print "[bot] Getting posts from Reddit"
    reddit=requests.get("http://www.reddit.com/r/{}/.json?limit=25".format(subreddit),   #25 hottest posts for front page
      headers={'User-Agent': 'my reddit bot 123',})
    submissions=reddit.json()["data"]["children"]
    for submission in submissions:
      post_content.append(strip_title(submission["data"]["title"]) + " redd.it/" + submission["data"]["id"])
      post_ids.append(submission["data"]["id"])
    return post_ids, post_content

def duplicate_check(id):   #Checks duplicate by seeing if file in in folder index with filename id
  return os.path.isfile('index/'+id)

def add_id_to_file(id):    #Makes empty file in folder index with filename id
  open('index/'+id, 'a').close

def main():
  post_ids, post_content = tweet_creator("leagueoflegends")
  tweeter(post_ids, post_content)

def tweeter(post_ids, post_content):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  for post, post_id in zip(post_content, post_ids):
    found = duplicate_check(post_id)
    if found == 0:
      print "[bot] Posting this link on twitter: " + post_id
      print post
      api.update_status(post)
      add_id_to_file(post_id)
      time.sleep(2)
    else:
      print "[bot] Already posted: " + post_id 

if __name__ == '__main__':
  main()