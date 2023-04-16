#WAP in python to accept a number form the user and check wehteher it is a prime number or an Automorphic number

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isAutomorphic(n):
    square = n * n
    while n > 0:
        if n % 10 != square % 10:
            return False
        n = n // 10
        square = square // 10
    return True

n = int(input("Enter a number: "))
if isPrime(n):

    print(n, "is a prime number")
else:

    print(n, "is not a prime number")
if isAutomorphic(n):

    print(n, "is an Automorphic number")
else:
            
        print(n, "is not an Automorphic number")
