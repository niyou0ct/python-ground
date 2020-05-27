def is_odd(n):
  return n % 2 == 1

data1 = [1, 2, 4, 5, 6, 10, 11]
data2 = filter(lambda x: x % 2 == 1, data1)
print(list(data2))