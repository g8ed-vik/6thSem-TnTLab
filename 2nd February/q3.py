#WAP in Python to find out the sum of digits of a number n by using function.

def sum (n):
    if n == 0:
        return 0
    else:
        return n%10 + sum(n//10)
    
x = sum(123)
print("The sum of digits of the number is", x)