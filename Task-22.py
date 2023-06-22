import random

array = []
summ = 0

for i in range(3):
    array.append(random.randint(1, 10))
    summ += array[i]

print(array)
print(summ)
