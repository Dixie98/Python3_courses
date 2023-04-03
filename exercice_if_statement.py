#This exercice simulate access to the program with password.
#Declare the variable password
password = 'Password123'

print("Enter the password :")
#Get User's value to the variable
inputed_password = input()
#Convert the variable to the string
inputed_password = str(inputed_password)

#If condition, acces denied, access granted
if inputed_password == password :
    print("Correct password")
    print("Access Granted")
else :
    print("Wrong password")
    print("Acces Denied")