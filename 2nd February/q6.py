#WAP in Python to calculate GCD/HCF of two numbers by using a iterative function for GCD.

def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)
    
x = gcd(12,18)
print("The GCD of the numbers is", x)