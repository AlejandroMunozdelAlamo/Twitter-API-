import os

#Función que muestra un menú por pantalla

def menu():

	os.system('cls')
	print "Seleccione una de las siguientes opciones"
	print "\t1 - Mostrar el usuario actual"
	print "\t2 - Mostrar el timeline del usuario actual"
	print "\t3 - Mostrar los usuarios que sigues y los que te siguen"
	print "\t4 - Obtener el ultimo tweet que aparece en la timeline del usuario actual"
	print "\t5 - Obtener el ultimo tweet enviado por el usuario actual"
	print "\t0 - Salir del programa"

while True:
	menu()
	opcionMenu = raw_input("Has seleccionado la opcion ")

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
		#Hacer una grafica cruzada para ver cuales de los friends del usuario son followers del mismo

	elif opcionMenu == "4":
		print ""
		obtener_last_tweet()

	elif opcionMenu == "5":	
		print ""
		obtener_last_tl_tweet()

	elif opcionMenu == "0":
		break

	else
		print ""
		raw_input("No ha seleccionado ninguna opcion del menu \nPulse una tecla para continuar")
