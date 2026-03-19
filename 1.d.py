def tipo_letra(letra):
    if letra.lower() in "aeiou":
        return "la letra es bocal"
    else:
        return "no es una vocal"
letra = input("ingrese una letra")
resultado = tipo_letra(letra)
print(resultado)
