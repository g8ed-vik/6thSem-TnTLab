#Write a program to check whether a number is prime or not in the given range
p = int(input("Enter lower  bound: "))
q = int(input("Enter upper bound: "))
n = int(input("Enter the value of n: "))
a= 0;
for x in range(p, q):
    if a == 2:
        print(" Not Prime")
else:
    print("Prime")    
