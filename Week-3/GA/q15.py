n = int(input())
value = ""
for i in range(n): 
    value+=input()*2+" " #here we are transforming each input by multiplying with 2(mapping) and then aggregating each term to a value.
print(value)