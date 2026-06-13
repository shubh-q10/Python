#Set is an unordered and mutable collection of lists
my_set = { "apple", 45, "seep", True }
empty_set = {}
print(my_set)
print(empty_set)

#mutable
my_set.add("Banana")
print(my_set)

#Valid Elements of Sets:


'''
Any immutable and hashable objects can be used as elements of sets. Eg. int, tuple, string.
Mutable objects like lists, sets and dictionaries cannot be used as elements of list.
Note -> item = (1, 2, [3, 4], 5). Here a is a tuple but still non-hashable as it  contains a list which is mutable. 
Hence `item` can’t be an element of a set.

'''


'''
set remove the duplicates automatically
'''

sety = {1, 2, 34, 2, 5, 7, 6, 6, 6, 8}
print(sety)