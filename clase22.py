#creando una funcion
def pedir_pizza():
	print("pedir pizza")
# fin de la funcion

pedir_pizza()


# inicia funcion con parametros
def checar_entrada(edad):
	if edad >= 21:
		print ("puedes entrar y chupar".upper())

	elif edad < 18:
		print("te la pelas putito")

	else:
		print("entrale pero chiton")
#fin de la funcion con parametros

#llamando a la funcion checar_entrada

checar_entrada(25)
