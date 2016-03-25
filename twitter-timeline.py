import twitter
import io
import json


def login():
	consumer_key = '2EtiJK3cvO2fcS1S2V7eynebC'
    consumer_secret = 'VSlhvNlGaweuT1s2tgVCrpCvdovxk83hlYFScxW7ooYvMPCOKn'
    oauth_token = '2324185926-sfZHWUetP1oy4ryrE0V2k7G7xBpkcPLf9Q8e1gm'
    oauth_token_secret = 'ASaiJnIfIGMgiTFiQoeTRAnJWb9MIzG0uZ7P0iOjzyOts'

    author = twitter.oauth.OAuth(oauth_token,oauth_token_secret,consumer_key,consumer_secret)
    api = twitter.Twitter(auth = author)
    return api
