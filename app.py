equipos = []

while True:
    print("\n--- INVENTARIO TI ---")
    print("1. Agregar equipo")
    print("2. Listar equipos")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del equipo: ")
        serie = input("Número de serie: ")

        with open("equipos.txt", "a") as archivo:
            archivo.write(f"{nombre} - {serie}\n")

        equipos.append({
            "nombre": nombre,
            "serie": serie
        })

        print("Equipo agregado.")

    elif opcion == "2":
        with open("equipos.txt", "r") as archivo:
            print(archivo.read())

    elif opcion == "3":
        break

    else:
        print("Opción inválida")