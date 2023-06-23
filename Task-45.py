try:
    file_name = input("Enter filename to read: ")
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error while reading file")
