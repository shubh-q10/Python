n = int(input())
value = None
for i in range(n):
  num = int(input())
  if value is None:
      value = num
  elif num < value:
      value = num
print(value)

#aggregation