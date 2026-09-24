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


def add_device():
    device_name = input("Device name: ")
    serial_number = input("Serial number: ")

    devices = load_devices()

    devices.append({
        "device_name": device_name,
        "serial_number": serial_number
    })

    save_devices(devices)

    print("Device added successfully.")


def list_devices():
    devices = load_devices()

    if not devices:
        print("No devices registered.")
        return

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


def search_device():
    serial_to_search = input(
        "Enter serial number: "
    )

    devices = load_devices()

    for device in devices:

        if device["serial_number"] == serial_to_search:

            print("\nDevice found:")
            print(
                f"Device: {device['device_name']}"
            )
            print(
                f"Serial: {device['serial_number']}"
            )
            return

    print("No device found with that serial number.")


def main():

    while True:

        print("\n--- IT INVENTORY SYSTEM ---")
        print("1. Add Device")
        print("2. List Devices")
        print("3. Search Device")
        print("4. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_device()

        elif option == "2":
            list_devices()

        elif option == "3":
            search_device()

        elif option == "4":
            print("Closing application...")
            break

        else:
            print("Invalid option.")


main()