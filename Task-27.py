import random

array = []

for i in range(6):
    array.append(random.randint(1, 10))

print(array)
print("Четные числа из списка: ")

for i in range(6):
    if (array[i] % 2 == 0):
        print(array[i])
