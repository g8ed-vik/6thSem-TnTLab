#Write a program in Python to check if a number is a prime number or not using recursion    

def is_prime(n, i=2):
    if n == 2:
        return True
    if n % i == 0 or n < 2:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")