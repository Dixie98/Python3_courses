#Provide 4 time try test user to choose a good number for the random game.
#Import random library
import random
#Declare Secret number
secret_number = random.randint(1,20)

#Prpare if inctruction to do the test 4 time

for i in range (1,4):
  #Declare user number and convert to integer
  user_number = int(input('Please enter the nomber: '))
  #Execute if condition to verify if those variables 
  #(secret number and user_number) are same value.
  if secret_number < user_number:
    print('Nice try, but your number is bigger than the secret number')
  elif secret_number > user_number:
    print('Nice try, but your number is smaller than the secret number')
  else:
   break

if user_number == secret_number:
  print('Congratulations !!!')
else:
  print('Sorry, maybe next time! The secret number is '+str(secret_number))
    
