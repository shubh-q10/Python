n = int(input())
value = None
for i in range(n):
  num = len(input())/2 #mapping
  if value is None:
      value = num #aggregation
  elif num < value:
      value = num
print(value)


