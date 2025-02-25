import tweepy

# Replace with your credentials
api_key = "MgBSSVwkY8hEfA7EQoD2Ghxnr"
api_secret = "wjTrfWfafan1KUl0jaKkV9ETXHsYsZsYbmpRgO2GyAH5LV3nQl"
access_token = "1341224503448227840-KZaydGhcXQFrv92F6MRkFXtDxzGz3Y"
access_token_secret = "k4xNkTqPOZLdpVN2WfmhSikTygNiNRbTzUhZrzLjs00NI"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Test with a simple call
try:
    user = api.verify_credentials()
    print("Authentication worked! Your username is:", user.screen_name)
except Exception as e:
    print("Error:", e)