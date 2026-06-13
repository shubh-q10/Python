l = [1, 2, 3, 4, 5, 78, "no", "hello"]
def remove_elements_at_two_indices(l: list, i1: int, i2: int):
    del l[i2]
    del l[i1]
    return l

print(remove_elements_at_two_indices(l, 3, 1))
