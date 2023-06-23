def get_min_number(numbers):
    numbers = [int(x) for x in numbers]
    min_number = min(numbers)
    return min_number


user_input = input("Enter a list of integers separated by commas: ").split(",")

try:
    result = get_min_number(user_input)
    print("Minimum number in the list:", result)

except ValueError:
    print("Error! Invalid numbers entered!")
