# Twitter API function: Obtain actual user's followars

import tweepy

main = login()

def mostrar_friends():
	user = main.me()
	followers = main.followers(user.id)
	print (f.name for f in followers)

