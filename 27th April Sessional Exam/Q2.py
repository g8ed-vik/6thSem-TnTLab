#WAP to calculate display the factorial of a number using recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
n =int(input("Enter number:"))

print("The factorial of", n, "is", factorial(n))