n = input(("Enter a string: "))
dict1 = {}

for i in n:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
        
print(dict1)