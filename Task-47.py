try:
    number = float(input("Enter the number: "))
    square = number * number
    print("Number square:", square)
except ValueError:
    print("Value Error")
