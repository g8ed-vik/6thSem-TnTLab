#WAP in python to accept a number and check whether it is a Niven number or not

def isNiven(n):
    sum = 0
    temp = n
    while n > 0:
        rem = n % 10
        sum = sum + rem
        n = n // 10
    if temp % sum == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if isNiven(n):
    print(n, "is a Niven number")
else:
    print(n, "is not a Niven number")
