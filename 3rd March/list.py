#intialize a list and print it

a = ['A', 'C', 'B', 'G']
b = ['X', 'E', 'F', 'D']
a.extend(b)
print(a)

#print length of list

c = len(a)
print(c)

#insert elements in list 
a.insert(2,"F")
print(a)

# count the number of specific element in list
a.insert(1,'A')
print(a.count('A'))

# remove specific element in list

a.remove('A')
print(a)

#pop element from a particular index in list

a.pop(2)
print(a)

#sort the list

a.sort()
print(a)


#reverse the list

a.reverse()
print(a)
