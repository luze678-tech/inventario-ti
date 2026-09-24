import json
import os

ARCHIVO = "equipos.json"


def cargar_equipos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    return []


def guardar_equipos(equipos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(equipos, archivo, indent=4)


while True:
    print("\n--- INVENTARIO TI JSON ---")
    print("1. Agregar equipo")
    print("2. Listar equipos")
    print("3. Buscar equipo")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        nombre = input("Nombre del equipo: ")
        serie = input("Número de serie: ")

        equipos = cargar_equipos()

        equipos.append({
            "nombre": nombre,
            "serie": serie
        })

        guardar_equipos(equipos)

        print("Equipo agregado correctamente.")

    elif opcion == "2":

        equipos = cargar_equipos()

        print("\n{:<20} {:<15}".format("EQUIPO", "SERIE"))
        print("-" * 35)

        for equipo in equipos:
            print(
                "{:<20} {:<15}".format(
                    equipo["nombre"],
                    equipo["serie"]
                )
            )

    elif opcion == "3":

        serie_buscar = input("Ingresa la serie a buscar: ")

        equipos = cargar_equipos()

        encontrado = False

        for equipo in equipos:

            if equipo["serie"] == serie_buscar:

                print("\nEquipo encontrado:")
                print(f"Nombre: {equipo['nombre']}")
                print(f"Serie: {equipo['serie']}")

                encontrado = True

        if not encontrado:
            print("No se encontró esa serie.")

    elif opcion == "4":

        print("Saliendo...")
        break

    else:
        print("Opción inválida.")