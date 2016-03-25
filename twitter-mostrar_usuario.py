# Twitter API function: Obtain actual user

import tweepy

main = login()

def mostrar_usuario():
	user = main.me()
	print user.id
	print user.name
	print user.screen_name
	print user.statuses_count
	print user.friends_count
	print user.followers_count
	if user.geo_enabled == True:
		print user.location
