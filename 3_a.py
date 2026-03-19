import random

def adivinar_numero():
    secreto = random.randint(1, 100)
    intento = 0

    while intento != secreto:
        intento = int(input("adivina el numero del 1 al 100: "))

        if intento < secreto:
            print("Es mayor")
        elif intento > secreto:
            print("Es menor")

    print("Good boyy")

adivinar_numero()
