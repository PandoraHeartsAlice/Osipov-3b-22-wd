arr = [5, 7, 11, 13, 15, 20, 25]
sum = 0
count = 0

for num in arr:
    if num > 10:
        sum += num
        count += 1

if count != 0:
    average = sum / count
    print("The arithmetic mean of elements greater than 10 is", average)
else:
    print("No elements greater than 10")
