def count_characters_frequency(input_string):
    frequency = {}

    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1

    for char, count in frequency.items():
        print(char, "-", count)


input_string = input("Enter the string: ")
count_characters_frequency(input_string)
