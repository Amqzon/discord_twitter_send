from twython import Twython
from api_keys import (
    api_key,
    api_key_secret,
    acces_token,
    acces_token_secret
)

twitter = Twython(
    api_key,
    api_key_secret,
    acces_token,
    acces_token_secret
)

def send_tweet(nachricht:str):

    twitter.update_status(status=nachricht)
    print(f"Tweet: {nachricht}")
