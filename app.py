import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Your Bearer Token (replace with your actual one)
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMEpzgEAAAAAEuoHiPyrkigB4RrSGwruhnHwlwc%3D7acFIGu9IPgkX5pJhKjfVmyYMIk8qi7560ZL0euZKOT9bVzNas"

# Authenticate with v2
client = tweepy.Client(bearer_token=bearer_token)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        keyword = request.form["keyword"]
        
        # Search for tweets with text and id
        tweets = client.search_recent_tweets(query=keyword, max_results=10, tweet_fields=["text", "id"])
        tweet_data = [{"text": tweet.text, "id": tweet.id} for tweet in tweets.data]
        tweet_texts = [tweet["text"] for tweet in tweet_data]  # For sentiment analysis

        # Analyze sentiment
        sentiments = []
        for tweet in tweet_texts:
            analysis = TextBlob(tweet)
            polarity = analysis.sentiment.polarity
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

        # Create bar chart
        plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'red', 'gray'])
        plt.title(f"Sentiment Analysis of Tweets about '{keyword}'")
        plt.xlabel("Sentiment")
        plt.ylabel("Number of Tweets")
        
        # Save chart to static folder
        chart_path = "static/sentiment_chart.png"
        plt.savefig(chart_path)
        plt.close()

        # Generate X URLs
        tweet_links = [{"text": tweet["text"], "url": f"https://twitter.com/user/status/{tweet['id']}"} for tweet in tweet_data]

        # Render results with tweet links
        return render_template("index.html", keyword=keyword, sentiment_counts=sentiment_counts, chart="sentiment_chart.png", tweets=tweet_links)
    
    # If GET, show empty form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)