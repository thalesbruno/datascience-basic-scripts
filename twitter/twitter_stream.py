# twitter_stream.py
import json
from collections import Counter
from twython import TwythonStreamer

tweets = []


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        """
        What do we do when Twitter sends us data?
        Here data will be a Python dict representing a tweet.
        """
        # if data.get('lang') == 'pt-br':
        tweets.append(data)
        # print(f"tweets received #{len(tweets)}")

        if len(tweets) >= 1000:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


with open('credentials.json', 'r') as f:
    credentials = json.load(f)

CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']
ACCESS_TOKEN = credentials['access_token']
ACCESS_TOKEN_SECRET = credentials['access_token_secret']

stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

stream.statuses.filter(track='data')

top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet["entities"]["hashtags"])

print(top_hashtags.most_common(5))
