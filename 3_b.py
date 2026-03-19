def contar_letra():
    texto = input("Ingresa una frase: ")
    letra = input("Ingresa una letra a buscar: ")
    contador = 0
    i = 0

    while i < len(texto):
        if texto[i] == letra:
            contador += 1
        i += 1

    print("La letra aparece", contador, "veces")

contar_letra()
