# Twitter API function: Obtain actual user's friends

import tweepy

main = login()

def mostrar_friends():
	user = main.me()
	friends = main.friends_ids(user.id)
	for f in friends
		name = main.get_user(f)
		print name