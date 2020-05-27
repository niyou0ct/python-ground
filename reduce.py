from functools import reduce

def add(arg1, arg2):
  return arg1 + arg2

x = reduce(lambda x, y: x + y, [1,2,3,4,5])
print(x)