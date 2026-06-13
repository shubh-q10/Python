'''
Write a function make_dict_from_elems_in_index that returns a dictionary consisting of a single key-value pair formed as follows:

the key is the element at the given index from the list keys.
the value is the element at the given index from the list values .
Assume the index is always within valid bounds for both lists.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

>>> keys = ['apple', 'banana', 'cherry']
>>> values = [10, 20, 30, 40]
>>> make_dict_from_elems_in_index(keys, values, 1) 
{'banana': 20}
>>> make_dict_from_elems_in_index(keys, values, -1) 
{'cherry': 40}

'''


keys = ['apple', 'banana', 'cherry']
values = [10, 20, 30, 40]

def make_dict_from_elems_in_index(keys, values, index:int)-> dict:
    new_d = dict()
    new_d[keys[index]] = values[index]
    return new_d

print(make_dict_from_elems_in_index(keys, values, 1))
