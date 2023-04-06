#d = {}
#d = {key1, value, key2, value}

d = {1: "A", 2: "B", 3: "C"}
for i in d:
    print(i)
d2 = d.copy()
print(d2)
print(d2.get(1))
print(d2.items())

#find frequency of each number using dictionary

a = [1,2,5,1,6,2,9]

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)