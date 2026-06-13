'''
and → returns the first falsy, else last.

or → returns the first truthy, else last

So and returns the first falsy value it finds, or the last value if all are truthy.
0 none " " false etc are falsy

'''
a = 5 or 2      # 5   (first truthy → returns it)
b = 0 or 2      # 2   (first falsy, second truthy → returns 2)
c = 0 or " ."     # ""  (both falsy → returns last one)

print(a)
print(b)
print(c)

