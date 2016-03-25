# Twitter API function: Obtain actual user's timeline

import tweepy

main = login()

def mostrar_timeline():
	user = main.me()
	timeline = main.user_timeline([id = user.id][count = 5])
	for status in timeline:
		print status.author
		print status.text
		print status.retweet_count
		

