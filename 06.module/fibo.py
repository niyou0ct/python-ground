# Fibonacci numbers module

def fib(n):
  a, b = 0, 1
  while a < n:
    print(a)
    a, b = b, a+b
  print()

def fib2(n):
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a + b
  return result

def display_str():
  yes_votes = 42_572_654
  no_votes = 43_132_495
  percentage = yes_votes / (yes_votes + no_votes)
  '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
