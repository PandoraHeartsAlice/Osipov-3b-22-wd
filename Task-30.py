text = input("Enter the string: ")

vowels = 0
consonants = 0

text = text.lower()

for char in text:
    if char.isalpha():
        if char in 'aeiouаеёиоуыэюя':
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
