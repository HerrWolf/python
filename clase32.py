try:
	a = int(input("Dame un numero: "))

	b = int(input("Dame otro numero: "))

except ValueError:
	print("Pon un numero puñetas")

else:
	suma = a + b

	print("La suma es: " + str(suma))
