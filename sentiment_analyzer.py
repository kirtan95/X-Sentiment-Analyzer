import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Your Bearer Token (replace with your actual one)
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMEpzgEAAAAAEuoHiPyrkigB4RrSGwruhnHwlwc%3D7acFIGu9IPgkX5pJhKjfVmyYMIk8qi7560ZL0euZKOT9bVzNas"

# Authenticate with v2
client = tweepy.Client(bearer_token=bearer_token)

# Search for tweets
keyword = "AI"
tweets = client.search_recent_tweets(query=keyword, max_results=10, tweet_fields=["text"])

# Get tweet text
tweet_texts = [tweet.text for tweet in tweets.data]

# Analyze sentiment
sentiments = []
for tweet in tweet_texts:
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity  # -1 (negative) to 1 (positive)
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    sentiments.append(sentiment)

# Count results
sentiment_counts = {
    "positive": sentiments.count("positive"),
    "negative": sentiments.count("negative"),
    "neutral": sentiments.count("neutral")
}

# Print results
print(f"Sentiment Analysis for '{keyword}' (based on {len(tweet_texts)} tweets):")
print(f"Positive: {sentiment_counts['positive']}")
print(f"Negative: {sentiment_counts['negative']}")
print(f"Neutral: {sentiment_counts['neutral']}")

# Create bar chart
plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'red', 'gray'])
plt.title(f"Sentiment Analysis of Tweets about '{keyword}'")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.show()