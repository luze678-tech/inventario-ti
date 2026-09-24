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

        print("Equipo agregado correctamente.")

    elif opcion == "2":
        print("\n{:<20} {:<15}".format("EQUIPO", "SERIE"))
        print("-" * 35)

        try:
            with open("equipos.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" - ")

                    if len(datos) == 2:
                        nombre, serie = datos
                        print("{:<20} {:<15}".format(nombre, serie))

        except FileNotFoundError:
            print("No hay equipos registrados.")

    elif opcion == "3":
        serie_buscar = input("Ingresa la serie a buscar: ")

        encontrado = False

        try:
            with open("equipos.txt", "r") as archivo:
                for linea in archivo:
                    if serie_buscar in linea:
                        print("\nEquipo encontrado:")
                        print(linea)
                        encontrado = True

            if not encontrado:
                print("No se encontró ningún equipo con esa serie.")

        except FileNotFoundError:
            print("No existe el archivo de equipos.")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")