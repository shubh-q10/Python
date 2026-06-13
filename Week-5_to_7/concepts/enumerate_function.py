# The enumerate() function in Python is used to iterate over an iterable (like a list, tuple, or string),
# while keeping track of the index of each item.

fruits = ["apple", "banana", "mango", "carrot"]
for index, fruit in enumerate(fruits):
    print( index, fruit)
    
    
for index, fruit in enumerate(fruits, start=1): #indexing start with 1
    print(index, fruit)
    



#EXAMPLE

l1 = ["eat", "sleep", "code", "repeat"]
s1 = "code"

obj1 = enumerate(l1)
obj2 = enumerate(s1)


print(list(obj1))
print(list(obj2))

print("Return type", type(obj1))
print(list(enumerate(l1)))

print(list(enumerate(s1, start=1)))

    