# Write a menu driven Python program to accept a number from the user and
# check whether it is a Palindrome or a Perfect number.
# (a) Palindrome number: (A number is a Palindrome which when read in reverse
# order is same as in the right order)
# Example: 11, 101, 151 etc.
# (b) Perfect number: (A number is called Perfect if it is equal to the sum of its
# factors other than the number itself.)
# Example: 6 = 1 + 2 + 3

def reverse(n):
    if n==0:
        return 0
    else:
        return (n%10)+reverse(n//10)
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum


while True:
    print("1. Insert")
    print("2. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        n=int(input("Enter a number: "))
        if(perfect(n)==n):
            print(n,"is a perfect number")
        elif(reverse(n)== n):
            print(n,"is a palindrome")
    
    elif ch==2:
        break
    print()