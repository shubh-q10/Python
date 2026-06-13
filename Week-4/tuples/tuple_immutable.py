'''
tuple is an ordered and immutable collection of items
Immutable → “unchangeable” → Once created, the object cannot be changed; if you try, 
Python makes a new object.

'''

emt_tuple = () #empty tuple
my_tup = ("apple", 2, True, "seep")
print(my_tup[0])
print(my_tup[1])

my_tup[0] = 56 #this will give an error coz tuple is immutable
print(my_tup)

