import tweepy #Importamos tweepy

#Función para acceder a Twitter
def login():

	consumer_key='2EtiJK3cvO2fcS1S2V7eynebC'
	consumer_secret='VSlhvNlGaweuT1s2tgVCrpCvdovxk83hlYFScxW7ooYvMPCOKn'
	access_token='2324185926-sfZHWUetP1oy4ryrE0V2k7G7xBpkcPLf9Q8e1gm'
	access_token_secret='ASaiJnIfIGMgiTFiQoeTRAnJWb9MIzG0uZ7P0iOjzyOts'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	return api


