def find_most_common_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # Finding the word with the maximum number of occurrences
        most_common_word = max(word_count, key=word_count.get)

    return most_common_word


filename = input("Enter a file name: ")

try:
    result = find_most_common_word(filename)
    print("The most frequent word in the file:", result)

except FileNotFoundError:
    print("Error! File not found!")
