#This programm compare two values when we enter two values
#the input
print("Enter value 1")
var_one = input()
print("Enter value 2")
var_two = input()
#If condition
if int(var_one) == int(var_two) :
    print(var_one + " and " + var_two + " are equal.")
elif int(var_one) < int(var_two) :
    print(var_one + " is lower than " + var_two + " .")
else :
    print(var_one + " is gretter than" + var_two + " .")