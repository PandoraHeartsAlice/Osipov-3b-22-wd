import random

array = []
for i in range(3):
    array.append(random.randint(1, 10))

print(array)
print("What number to find?")

if (array.count(int(input())) == 0):
    print("Number not found in array")
else:
    print("Number found in array")
