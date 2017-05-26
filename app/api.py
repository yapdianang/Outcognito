import requests
import requests_oauthlib

import secret


CONSUMER_KEY = 'oSBKtiz0OkQAVHf97bQZuNiU6'
ACCESS_TOKEN = '847921430628933633-oh8knJhaXveNWCTT8YM8tS3AMQo1cXP'

session = requests  # requests.Session() keep-alive seems to die eventually :/

def get(path, **params):
    return request('GET', path, **params)

def post(path, **params):
    return request('POST', path, **params)

def request(method, path, retry=True, **params):
    response = session.request(method, 'https://api.twitter.com/1.1/' + path + '.json',
                               params=params,
                               auth=requests_oauthlib.OAuth1(CONSUMER_KEY, secret.CONSUMER_SECRET,
                                                             ACCESS_TOKEN,
                                                             secret.ACCESS_TOKEN_SECRET))
    response.raise_for_status()
    return response.json()
