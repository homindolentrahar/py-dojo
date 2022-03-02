import sys
import clipboard
import json

CLIPBOARD_DATA = 'clipboard.json'


def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except:
        return {}


def save_data(file_path, string):
    with open(file_path, 'w') as file:
        json.dump(string, file)


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(CLIPBOARD_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()

        save_data(CLIPBOARD_DATA, data)
    elif command == "load":
        key = input("Enter a key: ")

        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key not found!")
    elif command == "list":
        print(data)
    else:
        print("Unknown command!")
else:
    print("Give exactly one command!")
