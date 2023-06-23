try:
    with open("test.txt", "w") as file:
        file.write("Hello, world!")
    print("Recording completed successfully")
except IOError:
    print("Error writing file")
