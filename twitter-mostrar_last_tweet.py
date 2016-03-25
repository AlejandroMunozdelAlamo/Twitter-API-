# Twitter API function: Obtain last user's tweet

import tweepy

main = login()

def mostrar_last_tweet():
	user = main.me()
	status = main.get_status(user.id)
	print status.text
	print retweet_count