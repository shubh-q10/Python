def remove_elements_at_two_indices(l: list, i1: int, i2: int):
    i1, i2 = sorted([i1, i2], reverse=True)
    l.pop(i1)
    l.pop(i2)
    return l
print(remove_elements_at_two_indices(["non", "list", "tree", "son", 23,], 1, 2))
    
