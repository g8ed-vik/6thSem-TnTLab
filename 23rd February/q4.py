#Write a program in Python to find the least common multiple of two numbers using recursion

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


def lcm(a, b):
    return (a * b) // hcf(a, b)


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("Lcm of", a, "and", b, "is", lcm(a, b))