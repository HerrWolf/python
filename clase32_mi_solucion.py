def suma():
	try:
		numero1 = int(input("Dame un numero: "))
		numero2 = int(input("Dame otro numero: "))

	except ValueError:
		print("Pon un numero puñetas")

	else:
		print("La suma es: " + str(numero1 + numero2))


suma()

suma()