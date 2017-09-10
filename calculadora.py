def suma():
	try:
		a = int(input("Dame un numero: "))
		b = int(input("Dame otro numero: "))

	except ValueError:
		print("Pon un numero puñetas")

	else:
		print("La suma es: " + str(a + b))

def resta():
	try:
		a = int(input("Dame un numero: "))
		b = int(input("Dame otro numero: "))

	except ValueError:
		print("Pon un numero puñetas")

	else:
		print("La resta es: " + str(a - b))

def multiplicacion():
	try:
		a = int(input("Dame un numero: "))
		b = int(input("Dame otro numero: "))

	except ValueError:
		print("Pon un numero puñetas")

	else:
		print("La suma es: " + str(a * b))


def division():
	try:
		a = int(input("Dame un numero: "))
		b = int(input("Dame otro numero: "))

	except ValueError:
		print("Pon un numero puñetas")

	else:
		print("La suma es: " + str(a / b))

repetir = 1
while repetir == 1:
    print("Bienvenidos a la calculadora \n"
          "Estas son las operaciones que puedes realizar\n"
          "1 - Suma\n"
          "2 - Resta\n"
          "3 - Multiplicacion\n"
          "4 - Division")

    operacion = int(input("Introduce el numero de operacion que quieres realizar: "))

    if operacion == 1:
        suma()

    elif operacion == 2:
        resta()

    elif operacion == 3:
        multiplicacion()

    elif operacion == 4:
        division()
    else:
        print("Elije un numero de operacion valido")

    cont = input("Desea continuar? SI/NO ")


    if cont == "no":
        repetir = 0

