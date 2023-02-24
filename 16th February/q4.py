# WAP to print fibonacci series using recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
def main():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(n):
            print(fibonacci(i))
