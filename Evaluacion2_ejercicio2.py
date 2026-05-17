print("=====ADIVINA EL NÚMERO=====")
intento = 0
respuesta1 = 0
respuesta2 = 0
from random import randint
while True:
    try:
        num1 = int(input("Ingrese el límite inferior: "))
        num2 = int(input("Ingrese el límite superior: "))
        if num1 < num2:
            break
        else:
            print("El límite inferior debe ser menor al límite superior.")
    except ValueError:
        print("Valor ingresado no es válido. Por favor, ingrese un número entero.")

numero = randint(num1, num2)
if numero % 2 != 0:
    if numero + 1 <= num2:
        numero += 1
    else:
        numero -= 1
while intento < 3:
    try:
        respuesta = int(input("Intente adivinar el número: "))
        if respuesta == numero:
            print(f"¡FELICIDADES! ADIVINASTE EL NÚMERO: {numero}")
            break
        elif respuesta > numero or respuesta < numero:
            intento += 1
            if intento == 1:
                respuesta1 = respuesta
                if respuesta > numero:
                    print(f"El número es menor a {respuesta}")
                else:
                    print(f"El número es mayor a {respuesta}")
            elif intento == 2:
                respuesta2 = respuesta
                if respuesta > numero:
                    print(f"El número es menor a {respuesta}")
                else:
                    print(f"El número es mayor a {respuesta}")
                diferencias1 = abs(respuesta1 - numero)
                diferencias2 = abs(respuesta2 - numero)
                if diferencias1 < diferencias2:
                    print(f"¡TE QUEDA SOLO UN INTENTO! El número {respuesta1} está más cerca que el número {respuesta2}.")
                elif diferencias2 < diferencias1:
                    print(f"¡TE QUEDA SOLO UN INTENTO! El número {respuesta2} está más cerca que el número {respuesta1}.")
            elif intento == 3:
                print(f"¡ALCANZASTE EL MÁXIMO DE INTENTOS! El número secreto era: {numero}")
                break
        else:
            print("Debes ingresar un valor válido.")
    except ValueError:
        print("Debes ingresar un número entero válido.")