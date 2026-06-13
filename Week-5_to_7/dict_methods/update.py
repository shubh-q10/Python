#UPDATING A DICTIONARY WITH ANOTHER DICTIONARY

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 5, 'c': 3}

dict1.update(dict2) #here key b is updated 
print(dict1)


#UPDATING WITH A LIST OF KEY-VALUE TUPLES

dict1 = {'x': 10, 'y': 20}
updates = [('y', 50), ('z', 30)]

dict1.update(updates)
print(dict1)


#UPDATING USING KEY WORD ARGUMENTS

person = {'name': 'Alice', 'age': 25}
person.update(age=26, city='New York') #here age is updated to 26

print(person)

#UPDATING WITH AN EMPTY DICTIONARY(means no change in dictionary)

data = {'a': 1, 'b': 2}
data.update({})
print(data)