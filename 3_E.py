def producto_hasta_negativo():
    producto = 1
    numero = 0

    while numero >= 0:
        numero = int(input("Ingresá un número: "))
        if numero >= 0:
            producto *= numero

    print("El producto total es:", producto)

producto_hasta_negativo()
