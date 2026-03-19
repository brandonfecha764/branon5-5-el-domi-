def obtener_dia(numero):
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miércoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sábado"
    elif numero == 7:
        return "Domingo"
    else:
        return "Error: número fuera de rango"

num = int(input("Ingresa un número del 1 al 7: "))
dia = obtener_dia(num)
print(dia)
