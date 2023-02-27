#WAP in Python to add two numbers entered through keyboard by using a suitable user defined function (say SUM) for addition operation.

def sum(a,b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a+b

x = sum(0,0)

print("Sum of two numbers is: ",x)