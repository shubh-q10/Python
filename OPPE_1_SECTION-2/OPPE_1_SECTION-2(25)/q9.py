# d1 = {'a': 1, 'b': 2}
# >>> d2 = {'b': 3, 'c': 4}
# >>> merge_dictionaries(d1, d2), 
# {'a': 1, 'b': 5, 'c': 4}

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {}
def merge_dictionaries(d1:dict, d2:dict):
    for key in d1:
        if key in d2:
            merged[key] = d1[key] + d2[key]
        else:
            merged[key] = d1[key]

    for key in d2:
        if key not in d1:
            merged[key] = d2[key]
    return merged
            
    
            
                
    
        
    
    
    
    
    
    
    
    
print(merge_dictionaries(d1, d2))
