#WAP in Python to test whether a number n is palindrome number or not.

def palindrome(n):
    temp = n
    reverse = 0
    while temp > 0:
        reverse = reverse*10 + temp%10
        temp = temp // 10
    return n == reverse
    
x = 121

if palindrome(x):
    print(x, "is a palindrome number")
else:
    print(x, "is not a palindrome number")