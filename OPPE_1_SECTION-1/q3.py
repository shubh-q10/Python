def remove_elements_at_two_indices(l:list, i1:int, i2:int):
    i1, i2 = sorted((i1, i2))
    
    l.pop(i2)
    l.pop(i1)
    return l

print(remove_elements_at_two_indices([1, 2, 3, 4, 5, 6, 7], 0, 1))