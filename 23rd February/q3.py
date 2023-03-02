#Write a program in Python to find GCD of two numbers using recursion

def gcd(a, b):  
    if b == 0:  
        return a  
    return gcd(b, a % b)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("GCD of", a, "and", b, "is", gcd(a, b))
