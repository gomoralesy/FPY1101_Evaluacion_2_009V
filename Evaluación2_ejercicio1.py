print("=====CÁLCULO DE VALORES EN MEDICAMENTOS=====")
Valor_medicamentos = 60000
envío_medicamentos = 8000
descuento_tramo = 0
descuento_medicamentos = 0
while True:
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser un número entero mayor a cero")
        except:
            print("Debe ingresar un número entero para la edad")
    while True:
        try:
            tramo = input("Ingrese el tramo a cual pertenece (A, B, C, D): ").upper()
            if tramo in ["A", "B", "C", "D"]:
                break
            else:
                print("El tramo debe ser una de las opciones: A, B, C, D")
        except:
            print("Debe ingresar una opción válida para el tramo")
    
#Validación de descuentos por edad
    if edad <= 30:
        if tramo == "A" or tramo == "B":
            descuento_medicamentos = 0.18
            descuento_tramo = 0.1
        elif tramo == "C" or tramo == "D":
            descuento_medicamentos = 0.12
    elif edad >= 31 and edad <=60:
        if tramo == "A" or tramo == "B":
            descuento_medicamentos = 0.12
            descuento_tramo = 0.1
        elif tramo == "C" or tramo == "D":
            descuento_medicamentos = 0.08
    elif edad > 60:
        print("No se aplican descuentos por edad para personas mayores de 60 años")
    
    if edad >= 55:
        descuento_tramo += 0.05
    else:
        descuento_tramo += 0
    
    Valor_medicamentos = Valor_medicamentos - (Valor_medicamentos * descuento_medicamentos)
    envío_medicamentos = envío_medicamentos - (envío_medicamentos * descuento_tramo)
    
    print(f"Valor de medicamentos: ${Valor_medicamentos}")
    print(f"Valor del despacho: ${envío_medicamentos}")
    break
print("Gracias por usar nuestro sistema de cálculo de descuentos en medicamentos")
