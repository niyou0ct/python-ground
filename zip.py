data1 = [1, 2, 3, 4, 5]
data2 = ['a', 'b', 'c', 'd', 'd']

for idx, (x, y) in enumerate(zip(data1, data2)):
  print(idx, x, y)