import random
import time

pos1 = 0
pos2 = 0
tiempo = 0

print("Que haces nene? bueno, para este programa vamos a simular una carrera entre dos corredores. Cada corredor avanzará una distancia aleatoria entre 1 y 10 metros cada segundo. El primero en llegar a los 100 metros gana un pedido gratis.")

while pos1 < 100 and pos2 < 100:
    avance1 = random.randint(1, 10)
    avance2 = random.randint(1, 10)
    
    pos1 += avance1
    pos2 += avance2
    tiempo += 1
    
    print(f"Segundo {tiempo:2d} → Corredor 1: {pos1:3d}m | Corredor 2: {pos2:3d}m")
    time.sleep(0.5)

if pos1 >= 100 and pos2 >= 100:
    print("¿Como empatas una carrera? jajaja no se pero empataron")
elif pos1 >= 100:
    print(f"BIEN NENE GANASTE SO' RE CRA', ahora llega un veneco que te trae tu pedido. llegaste en {tiempo} segundos")
else:
    print(f"Uh que choto q so' nene, perdiste contra un bolita, no importa igual. el otro llego en {tiempo} segundos")

#me atudo igor
