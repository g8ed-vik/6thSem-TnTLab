p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

for n in  range(p,q):
    a = 0
    for x in range (1, n+1):
        if n % x == 0:
            a += 1
    if a == 2:
        print(n, "Prime")