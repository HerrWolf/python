#ciclos while

manzanas = 10
while manzanas > 0:
	print("Me estoy comiendo una manzana " + str(manzanas))
	manzanas -=1

print("Me quede sin mazanas")


#ciclo for

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

# for numero in lista_numeros:
# 	if numero > 5:
# 		break #esto rompe el ciclo for
# 	print(numero)


for numero in lista_numeros:
	if numero == 5:
		continue #esto salta el ciclo for un lugar
	print(numero)