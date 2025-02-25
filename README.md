# X Sentiment Analyzer

A Flask web app that fetches tweets from X, analyzes sentiment, and displays results with a chart and clickable tweet links.

## Features
- X-themed web interface with modern CSS and tweet links
- Fetches tweets using X API v2
- Sentiment analysis with TextBlob
- Bar chart visualization with Matplotlib
- Rate limit note for X API (50 requests/15 min)

## Setup
1. Install dependencies: `pip install tweepy textblob matplotlib flask`
2. Add your X API Bearer Token to `app.py`
3. Run: `python app.py`
4. Visit: `http://127.0.0.1:5000/`
