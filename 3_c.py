def suma_hasta_negativo():
    suma = 0
    numero = 0

    while numero >= 0:
        numero = int(input("Ingresá un número: "))
        if numero >= 0:
            suma += numero

    print("La suma total es:", suma)

suma_hasta_negativo()
