# //print grades of students

mk = int(input("Enter marks : "))
if (mk <=100 & mk >= 90):
    print("O")
elif (mk >= 80 & mk < 90):
    print("E") 
elif (mk >= 70 & mk < 80):
    print("A")
elif (mk >= 60 & mk < 70):
    print("B")
elif (mk >= 50 & mk < 60):
    print("C")
elif (mk >= 40 & mk < 50):
    print("D")
else:
    print("F")
                 