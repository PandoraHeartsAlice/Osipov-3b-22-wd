import random

array = []
sort_array = []

for i in range(10):
    array.append(random.randint(1, 100))

sort_array = array
sort_array.sort()

print(array)
print("Наименьшее -", sort_array[0], "наибольшее -", sort_array[9])
