#Write a program in Python to convert a decimal number to binary using recursion

def dec_to_bin(n):
    if n == 0:
        return 0
    return n % 2 + 10 * dec_to_bin(n // 2)

n = int(input("Enter a number: "))
print("Binary of", n, "is", dec_to_bin(n))
