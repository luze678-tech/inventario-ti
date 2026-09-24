import json
import os

FILE_NAME = "devices.json"


def load_devices():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


def save_devices(devices):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(devices, file, indent=4)


while True:
    print("\n--- IT INVENTORY SYSTEM ---")
    print("1. Add Device")
    print("2. List Devices")
    print("3. Search Device")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":

        device_name = input("Device name: ")
        serial_number = input("Serial number: ")

        devices = load_devices()

        devices.append({
            "device_name": device_name,
            "serial_number": serial_number
        })

        save_devices(devices)

        print("Device added successfully.")

    elif option == "2":

        devices = load_devices()

        print("\n{:<25} {:<20}".format(
            "DEVICE NAME",
            "SERIAL NUMBER"
        ))
        print("-" * 45)

        for device in devices:
            print(
                "{:<25} {:<20}".format(
                    device["device_name"],
                    device["serial_number"]
                )
            )

    elif option == "3":

        serial_to_search = input(
            "Enter serial number: "
        )

        devices = load_devices()

        device_found = False

        for device in devices:

            if device["serial_number"] == serial_to_search:

                print("\nDevice found:")
                print(
                    f"Device: {device['device_name']}"
                )
                print(
                    f"Serial: {device['serial_number']}"
                )

                device_found = True

        if not device_found:
            print("No device found with that serial number.")

    elif option == "4":

        print("Closing application...")
        break

    else:
        print("Invalid option.")