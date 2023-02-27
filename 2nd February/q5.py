#WAP in Python to swap the values of two variables by using a suitable user defined function

def swap(a,b):
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    temp = a
    a = b
    b = temp
    
    return a,b

x = swap(0,0)
print("The swapped values are",x, "for a = 5 and b = 10")