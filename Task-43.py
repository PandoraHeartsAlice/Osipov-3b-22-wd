try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the first number: "))

    if num2 == 0:
        raise ZeroDivisionError

    result = num1 / num2
    print("The result of the division:", result)

except ValueError:
    print("Error: invalid data entered")

except ZeroDivisionError:
    print("Error: division by zero")
