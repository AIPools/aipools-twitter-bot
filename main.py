# main.py

import tweepy
import openai
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, OPENAI_API_KEY
from prompts import TWEET_PROMPT

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def create_tweet():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You're an AI crypto bot posting edgy, viral tweets."},
            {"role": "user", "content": TWEET_PROMPT}
        ]
    )
    return response.choices[0].message.content.strip()

def post_tweet(tweet_text):
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )
    client.create_tweet(text=tweet_text)
    print("✅ Tweeted:", tweet_text)

if __name__ == "__main__":
    tweet = create_tweet()
    post_tweet(tweet)
