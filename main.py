# main.py

import tweepy
import openai
import time
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, OPENAI_API_KEY
from prompts import TWEET_PROMPT

def create_tweet():
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're an AI crypto bot posting edgy, viral tweets."},
            {"role": "user", "content": TWEET_PROMPT}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def post_tweet(tweet_text):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(tweet_text)
    print("✅ Tweeted:", tweet_text)

if __name__ == "__main__":
    tweet = create_tweet()
    post_tweet(tweet)
