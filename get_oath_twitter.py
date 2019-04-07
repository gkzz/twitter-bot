from requests_oauthlib import OAuth1Session
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class GetOathOfTwitter:
    
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.consumer_key = CONSUMER_KEY
        self.consumer_secret = CONSUMER_SECRET
        self.access_token = ACCESS_TOKEN
        self.access_token_secret = ACCESS_TOKEN_SECRET

    
    def get_oath(self):
        client = OAuth1Session(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret,
        )
        return client


    def test_run(self, client):
       sample_text = "This is a test."
       params = {"status": sample_text + " "}
       client.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

obj = GetOathOfTwitter(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
client = obj.get_oath()
obj.test_run(client)
