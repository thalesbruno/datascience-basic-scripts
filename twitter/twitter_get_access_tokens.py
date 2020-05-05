# twitter.py
import json
import webbrowser
from twython import Twython

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']

# Get a temporary client to retrieve an authetication URL
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds['auth_url']

# Now visit that URL to authorize the application and get a PIN
print(f"go visit {url} and get the PIN code and past it below")
webbrowser.open(url)
PIN_CODE = input("please enter the PIN code: ")

# Now we use that PIN_CODE to get the actual tokens
auth_client = Twython(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      temp_creds['oauth_token'],
                      temp_creds['oauth_token_secret'])
final_step = auth_client.get_authorized_tokens(PIN_CODE)
ACCESS_TOKEN = final_step['oauth_token']
ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']

print(f"access token: {ACCESS_TOKEN}")
print(f"access token secret: {ACCESS_TOKEN_SECRET}")
