try:
    N = int(input("Enter an integer N: "))

    if N <= 0:
        print("Entered non-positive number")
    else:
        sum = (N * (N + 1)) // 2

        print("The sum of numbers from 1 to", N, "is", sum)

except ValueError:
    print("Not an integer entered")
