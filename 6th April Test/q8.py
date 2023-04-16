# Write a python function passwordGen(), that will validate the string with following
# property
# a. The string should contain at least one Capital letter
# b. The string should contain at least one small letter
# c. The string should contain at least one special symbol
# d. The string should contain at least one digit
# e. The string should contain the user name as substring
#it will also take username as input with password and check if the password contains the username as substring

def passwordGen():
    userName = input("Enter the username: ")
    password = input("Enter the password: ")
    if password.isalnum():
        print("Password should contain at least one special character")
    if password.isalpha():
        print("Password should contain at least one digit")
    if password.islower():
        print("Password should contain at least one Capital letter")
    if password.isupper():
        print("Password should contain at least one small letter")
    if userName not in password:
        print("Password should contain the username as substring")
    else:
        print("Password is valid")
        
passwordGen()