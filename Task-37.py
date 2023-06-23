def find_two_smallest(numbers):
    if len(numbers) < 2:
        print("You must pass at least two numbers.")
        return

    smallest = min(numbers)
    numbers.remove(smallest)
    second_smallest = min(numbers)

    print(f"The two smallest values: {smallest} and {second_smallest}")


numbers = [5, 2, 7, 3, 9, 1]
find_two_smallest(numbers)
