#WAP in Python to find the factorial of a number n by using a suitable user defined function for it.

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
x = fact(5)
print("The factorial of the number is", x, "for n = 5") 