def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_of_arrays(arr1, arr2):
    for num in arr1[1:]:
        arr2 = [gcd(num, x) for x in arr2]
    return arr2[0]


arr1 = [24, 36, 48, 60]
arr2 = [12, 18, 24, 36, 72]

result = gcd_of_arrays(arr1, arr2)
print(result)
