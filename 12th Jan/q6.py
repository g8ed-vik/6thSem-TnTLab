# //WAP to determine whether year entered through keyboard is leap year or not

yr = int(input("Enter year : "))

if (yr%400==0) and (yr%100==0):
    print(yr," is leap year")
elif(yr%4==0) and (yr%100 !=0):
    print(yr," is leap year")
else:
    print(yr," is not leap year")
    
    