import random

def getNumber(number):
    if number == 1:
      return 'The number is equal 1'
    elif number == 2:
      return 'The number is equal 2'
    elif number == 3:
      return 'The number is equal 3'
    elif number == 4:
      return 'The number is equal 4'
    elif number == 5:
      return 'The number is equal 5'

#Add random value between 1 and 5  
get_random_number = random.randint(1,5)
 
test_random_number = getNumber(get_random_number)

print(test_random_number)