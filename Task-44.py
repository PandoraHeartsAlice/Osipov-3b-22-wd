try:
    with open("test.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
