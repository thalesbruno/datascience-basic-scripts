# twitter.py
import json
from twython import Twython

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']
ACCESS_TOKEN = credentials['access_token']
ACCESS_TOKEN_SECRET = credentials['access_token_access']
