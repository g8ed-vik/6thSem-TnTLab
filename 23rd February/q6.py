#Write a program in Python to reverse a string. Use recursion.

def reverse_string(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + reverse_string(str[:-1])
    
str = input("Enter a string: ")
print("Reverse of", str, "is", reverse_string(str))