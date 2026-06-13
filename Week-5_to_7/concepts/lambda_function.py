cube = lambda x: x*x*x
print("cube of 5 is:", cube(5))

add = lambda a, b, c: a + b + c
print("addition of 2, 3, 5:", add(2, 3, 5))

from functools import reduce
numbers = [1, 2, 3, 4, 5]
addition = reduce(lambda x, y: x + y, numbers)
print("addition of numbers is", addition)