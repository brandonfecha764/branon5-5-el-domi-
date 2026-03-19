def suma_impares():
    numero = int(input("Pone tu numero bb: "))
    suma = 0

    for i in range(1, numero + 1):
        if i % 2 != 0:
            suma += i

    print("La suma de la vaina ez:", suma)

suma_impares()
