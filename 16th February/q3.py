#WAP to print factorial of n numbers using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print(factorial(n))
    
    