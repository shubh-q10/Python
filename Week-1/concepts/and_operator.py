'''
and → returns the first falsy, else last.

or → returns the first truthy, else last

So and returns the first falsy value it finds, or the last value if all are truthy.
0 none " " false etc are falsy

'''

#

a = 5 and 2      # 2   (first truthy → gives second)
b = 0 and 2      # 0   (first falsy → stops there)
c = 5 and 0      # 0   (second falsy → returns 0)


print(a)
print(b)
print(c)
