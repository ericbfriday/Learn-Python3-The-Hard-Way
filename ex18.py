def print_two(*args):
  args1, args2 = args
  print(f'args1: {args1}, args2: {args2}')

def print_two_again(arg1, arg2):
  print(f'arg1: {arg1}, arg2: {arg2}')

def print_one(arg):
  print(f'arg: {arg}')

def print_none():
  print('Nothing here...')

print_two('Bob', 'Sam')
print_two_again('Bobby', 'Sammy')
print_one('Pedro')
print_none()