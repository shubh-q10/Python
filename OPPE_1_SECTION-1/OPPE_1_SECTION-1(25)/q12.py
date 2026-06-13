keys = ['apple', 'banana', 'cherry']
values = [10, 20, 30, 40]

def make_dict_from_elems_in_index(keys, values, index:int)-> dict:
    return {keys[index]:values[index]}

print(make_dict_from_elems_in_index(keys, values, 1))