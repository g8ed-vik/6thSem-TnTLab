# WAP in python to convert given paisa to equivalent rupees and paise

p = int(input("Enter paisa : "))
r = int(p/100)
p1 = p%100
print("Rupees : ",r , "Paise : ",p1)
