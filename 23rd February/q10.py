#Write a program in Python to check whether a given String is Palindrome or not using recursion

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

s = input("Enter a string: ")
if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
    
    