# WAP in python to print first 50 natural numbers using recursion

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n)
        
if __name__ == '__main__':
    printN(50)

