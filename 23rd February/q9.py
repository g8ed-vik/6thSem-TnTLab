#Write a program in Python to print even or odd numbers in a given range using recursion

def even_odd(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
    return even_odd(n - 1)

n = int(input("Enter a number: "))
even_odd(n)
