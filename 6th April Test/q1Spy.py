#WAP in python to accept a number and check whether it is a spy number or not

def isSpy(n):
    sum = 0
    product = 1
    while n > 0:
        rem = n % 10
        sum = sum + rem
        product = product * rem
        n = n // 10
    if sum == product:
        return True
    else:
        return False
    
n = int(input("Enter a number: "))
if isSpy(n):
    print(n, "is a spy number")
else:
    print(n, "is not a spy number")
