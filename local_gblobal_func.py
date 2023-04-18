def func():
  number = 30
  print(number)
  
  
func()

number = 15
print(number)
func()

def func_two():
  global number_two
  number_two = 25
  
number_two = 30
print(number_two)
func_two()

def func_tree(number):
  number +=1
  return number

number = func_tree(number)
print(number)