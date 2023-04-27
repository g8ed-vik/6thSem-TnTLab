# Write a menu driven python program to input a number and display the new
# number after reversing the digits of the original number. The program also
# displays the absolute difference between the original number and the reversed
# number.

def reverse(n):
    if n==0:
        return 0
    else:
        return (n%10)+reverse(n//10)

while True:
    print("1. Insert")
    print("2. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        n=int(input("Enter a number: "))
        print(reverse(n))
    elif ch==2:
        break
    print()