class User():
  def __init__(self, attrs):
    for k, v in attrs.items():
      setattr(self, k, v)

obj = User({'name': 'Kuro', 'age': 30, 'memo': 'very cool!'})
print(obj.name)
print(obj.age)
print(obj.memo)
