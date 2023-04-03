try_number = 5
i = 0
while i != 100 :
  print("Enter any number: ")
  print("You have " +str(try_number)+ " attempt")
  i = input()
  try_number -= 1
  if try_number == 0 : 
    print("Sorry, you have used all attempt")
    break
    