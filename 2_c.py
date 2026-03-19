def mostrar_tablas():
    for i in range(1, 11):
        print("Tabla del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

mostrar_tablas()
