#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import re
import numpy as np
import matplotlib.pyplot as plt

user_id = 'u\'id: *?,'
user_name ='u\'name: *?,'
user_screen_name ='u\'screen_name: *?,'
description ='u\'description: *?,'
user_status_text ='u\'text: *?,'
follow_req ='u\'follow_request_sent: *?,'
friends_count ='u\'friends_count: *?,'
followers_count ='u\'followers_count: *?,'
numbering = "\t -> "

# Funcion que nos identifica y nos permite acceder a la API

def login():

	consumer_key='2EtiJK3cvO2fcS1S2V7eynebC'
	consumer_secret='VSlhvNlGaweuT1s2tgVCrpCvdovxk83hlYFScxW7ooYvMPCOKn'
	access_token='2324185926-sfZHWUetP1oy4ryrE0V2k7G7xBpkcPLf9Q8e1gm'
	access_token_secret='ASaiJnIfIGMgiTFiQoeTRAnJWb9MIzG0uZ7P0iOjzyOts'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	return api

main = login()

# Funcion que muestra los datos del usuario
def mostrar_datos_usuario(user):
	print "\tUser_ID : " + str(user.id)
	print "\tUser_name : " + user.name
	print "\tUser_screen_name : " + user.screen_name
	print "\tUser_description : " + user.description
	print "\tUser_tweets_count : " + str(user.statuses_count)
	print "\tUser_friends : " + str(user.friends_count)
	print "\tUser_followers : " + str(user.followers_count)
	if user.geo_enabled == True:
		print "\tUser_location : " + str(user.location)
	print "\n"

# Funcion que muestra los datos de un tweet (estado)
def mostrar_datos(estado):
	print "\tAuthor : " + str(estado.author.screen_name) #Obtener nombre original
	print "\tStatus_description : " + estado.text.encode('utf-8')
	print "\tRetweets_count : " + str(estado.retweet_count)
	print "\tFavorite_count : " + str(estado.favorite_count)
	print "\t-------------------------------------------------------------------------"
	print "\n"

# Funcion que muestra los datos del usuario actual
def mostrar_usuario():
	mostrar_datos_usuario(main.me())

# Funcion que muestra el timeline del usuario actual
def mostrar_timeline():
	user = main.me()
	timeline = main.user_timeline(user.id)
	for i in timeline:
		mostrar_datos(i)

# Funcion que muestra el nombre de los friends del usuario actual
def mostrar_friends():
	user = main.me()
	friends = main.friends_ids(user.id)
	print("\tFriends List :\n")
	for f in friends:
		name = main.get_user(f).screen_name
		print numbering.encode('utf-8') + name
	print "\n"

# Funcion que muestra el nombre de los followers del usuario actual
def mostrar_followers():
	user = main.me()
	followers = main.followers_ids(user.id)
	print("\tFollowers List :\n")
	for f in followers:
		name = main.get_user(f).screen_name
		print numbering.encode('utf-8') + name
	print "\n"

# Funcion que mustra los seguidores de los N primeros seguidores del usuario actual
def grafica():
	user = main.me()
	followers = main.followers(user.id)
	x = list()
	y = list()
	print " Introduzca el numero de seguidores que desee mostrar en la gráfica"
	N = input()
	for usuario in followers[1:N]:
		x += [usuario.screen_name]			# nombres de los seguidores
		y += [usuario.followers_count]		# numero de seguidores

	ind = np.arange(len(x))    	# the x locations for the groups
	width = 0.5   		# the width of the bars: can also be len(x) sequence

	p2 = plt.bar(ind, y, width, color='y')

	plt.ylabel('Numero de seguidores')
	plt.title('Numero de seguidores / nombres')
	plt.xticks(ind + width/2., x)
	plt.yticks(np.arange(0, max(y), 30))

	plt.show()


# Función del Menú Principal
def menu():

	menu = {}
	menu[''] = "\t Menu Principal: \n"
	menu['\t1'] = " - Mostrar el usuario actual"
	menu['\t2'] = " - Mostrar el timeline del usuario actual"
	menu['\t3'] = " - Mostrar los usuarios que sigues y los que te siguen"
	menu['\t4'] = " - Mostrar gráfica followers de mis N primeros followers"
	menu['\t5'] = " - Salir de la aplicacion\n"

	while True:
		options=menu.keys()
		options.sort()
		for entry in options:
			print entry, menu[entry]

		opcionMenu=raw_input(" Por favor, seleccione una opcion\n Opcion seleccionada: ")

		if opcionMenu == "1":
			print ""
			mostrar_usuario()

		elif opcionMenu == "2":
			print ""
			mostrar_timeline()

		elif opcionMenu == "3":
			print ""
			mostrar_friends()
			print ""
			mostrar_followers()
			
		elif opcionMenu == "4":
			print ""
			grafica()

		elif opcionMenu == "5":
			print " Muchas gracias. Esperamos que la aplicacion le haya sido de utilidad\n"
			break

print "\n Twitter Api Workshop\n Aplicación realizada por Abel Castilla Rodriguez y Alejandro Munoz del Alamo\n"
menu()