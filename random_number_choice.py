import random

def func_check(number) :
  if number == random_number:
      print('Your number is equal to random number')
      print('Congratulations !!!')
  elif number > random_number:
    print('Your number is higher than random number, the random number is ' +str(random_number))
  else :
    print('Your number is lower than random number, the random number is ' +str(random_number))

random_number = random.randint(0,10)

user_number = int(input('Enter the number: '))

launch_test = func_check(user_number)