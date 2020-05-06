# twitter.py
import json
from twython import Twython

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']
ACCESS_TOKEN = credentials['access_token']
ACCESS_TOKEN_SECRET = credentials['access_token_secret']

twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)

# Checking credentials
# twitter.verify_credentials()

# Search for tweet containing the phrase "data science"
for status in twitter.search(q='"brumado"')['statuses']:
    user = status['user']['screen_name']
    text = status['text']
    print(f"{user}: {text}\n")
