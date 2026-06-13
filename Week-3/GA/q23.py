n = int(input())
value = None
for i in range(n):
  num = len(input()) #mapping coz we are transforming each num to len of num
  if value is None:
      value = num
  elif num/2 < value: 
      value = num
print(value)


#mapping and aggregation