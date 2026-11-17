import tweepy
from collections import Counter
import re

# Enter Twitter API Bearer Token
token = input("Enter Bearer Token: ")

client = tweepy.Client(bearer_token=token)

# Search tweets
topic = input("Enter topic: ")

tweets = client.search_recent_tweets(
    query=topic + " -is:retweet",
    max_results=100,
    tweet_fields=["created_at"]
)

words = []
entities = []

if tweets.data:

    for tweet in tweets.data:

        print("\nTweet:", tweet.text)
        print("Date:", tweet.created_at)

        words.extend(re.findall(r'\b[a-zA-Z]{3,}\b',
                                tweet.text.lower()))

        entities.extend(re.findall(r'@[a-zA-Z0-9_]+',
                                   tweet.text))

# Find trending words
print("\nTrending Words:")

for word, count in Counter(words).most_common(10):
    print(word, ":", count)

# Find named entities
print("\nNamed Entities / User Mentions:")

for entity, count in Counter(entities).most_common(10):
    print(entity, ":", count)