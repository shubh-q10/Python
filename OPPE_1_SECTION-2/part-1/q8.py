def merge_dictionaries(d1:dict, d2:dict):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

print(merge_dictionaries({'a': 1, 'b': 2},{'b': 3, 'c': 4}))

    
