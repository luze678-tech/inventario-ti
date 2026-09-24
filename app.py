equipos = []

while True:
    print("\n--- INVENTARIO TI ---")
    print("1. Agregar equipo")
    print("2. Listar equipos")
    print("3. Buscar equipo")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del equipo: ")
        serie = input("Número de serie: ")

        with open("equipos.txt", "a") as archivo:
            archivo.write(f"{nombre} - {serie}\n")

        print("Equipo agregado.")

    elif opcion == "2":
        with open("equipos.txt", "r") as archivo:
            print(archivo.read())

    elif opcion == "3":
        serie_buscar = input("Ingresa la serie a buscar: ")

        encontrado = False

        with open("equipos.txt", "r") as archivo:
            for linea in archivo:
                if serie_buscar in linea:
                    print("Equipo encontrado:")
                    print(linea)
                    encontrado = True

        if not encontrado:
            print("No se encontró ningún equipo con esa serie.")

    elif opcion == "4":
        break

    else:
        print("Opción inválida")