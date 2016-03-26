#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import os
import re
import pprint

user_id = 'u\'id: *?,'
user_name ='u\'name: *?,'
user_screen_name ='u\'screen_name: *?,'
description ='u\'description: *?,'
user_status_text ='u\'text: *?,'
follow_req ='u\'follow_request_sent: *?,'
friends_count ='u\'friends_count: *?,'
followers_count ='u\'followers_count: *?,'


def expresion(cadena):

	patron = re.compile(user_id)
	for m in patron.finditer(cadena):
		if (cadena == user_id):
			print "\t → %s : %s " %("ID_usuario :", m.group(0))
		elif (cadena == user_screen_name):
			print "\t → %s : %s " %("Nombre_publico :", m.group(0))
		elif (cadena == user_name):
			print "\t → %s : %s " %("Nombre_usuario :", m.group(0))
		elif (cadena == description):
			print "\t → %s : %s " %("Descripcion :", m.group(0))
		elif (cadena == user_status_text):
			print "\t → %s : %s " %("Estado actual :", m.group(0))
		elif (cadena == follow_req):
			print "\t → %s : %s " %("Solicitud para seguir :", m.group(0))
		elif (cadena == friends_count):
			print "\t → %s : %s " %("Personas a las que sigue :", m.group(0))
		elif (cadena == followers_count):
			print "\t → %s : %s " %("Seguidores:", m.group(0))
		print "---------------------------------------------------------------"



# Funcion que muestra un menu por pantalla

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

def mostrar_datos(user):
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

def mostrar_datos(estado):
	pprint.pprint(estado)
	type(estado.text)
	print "\tAuthor : " + str(estado.screen_name) #Obtener nombre original
	#print "\tStatus_description : " + str(unicode(estado.text()))
	print "\tRetweets_count : " + str(estado.retweet_count)
	print "\tFavorite_count : " + str(estado.favorite_count)
	print "\n"

def mostrar_usuario():
	mostrar_datos(main.me())


def mostrar_timeline():
	user = main.me()
	timeline = main.user_timeline(user.id)
	for i in timeline:
		mostrar_datos(i)

		
		
def mostrar_friends():
	user = main.me()
	friends = main.friends_ids(user.id)
	for f in friends:
		name = main.get_user(f)
		print name
	print "\n"


def mostrar_followers():
	user = main.me()
	followers = main.followers(user.id)
	print (f.name for f in followers)
	print "\n"

def mostrar_last_tweet():
	user = main.me()
	status = main.get_status(user.id)
	print status.text
	print retweet_count
	print "\n"

def menu():

	menu = {}
	menu[''] = "\t Menu Principal: \n"
	menu['\t1'] = " - Mostrar el usuario actual"
	menu['\t2'] = " - Mostrar el timeline del usuario actual"
	menu['\t3'] = " - Mostrar los usuarios que sigues y los que te siguen"
	menu['\t4'] = " - Salir de la aplicacion\n"

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
			expresion(mostrar_friends())
			print ""
			expresion(mostrar_followers())
			#mostrar_followers()
			#Hacer una grafica cruzada para ver cuales de los friends del usuario son followers del mismo

		elif opcionMenu == "4":
			print " Muchas gracias. Esperamos que la aplicacion le haya sido de utilidad\n"
			break

print "\n Twitter Api Workshop\n Aplicacion realizada por Abel Castilla Rodriguez y Alejandro Munoz del Alamo\n"
menu()