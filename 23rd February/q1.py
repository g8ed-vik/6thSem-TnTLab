#Write a program in Python to count the digits of a given number using recursion

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

n = int(input("Enter a number: "))
print("Number of digits in", n, "is", count_digits(n))

