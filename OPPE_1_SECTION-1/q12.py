def is_present_in_opposite_halves(elem, l1: list, l2: list):
    mid1 = len(l1) // 2
    mid2 = len(l2) // 2
    
    in_l1_first = elem in l1[:mid1]
    in_l1_second = elem in l1[mid1:]
    
    in_l2_first = elem in l2[:mid2]
    in_l2_second = elem in l2[mid2:]
    
    return (in_l1_first and in_l2_second) or (in_l2_first and in_l1_second)


print(is_present_in_opposite_halves(3, [1, 2, 3, 4], [5, 6, 3, 8]))
print(is_present_in_opposite_halves(7, [1, 2, 3, 4], [5, 6, 3, 8]))
print(is_present_in_opposite_halves(6, [5, 6, 7, 8], [1, 2, 6, 4]))
print(is_present_in_opposite_halves(6, [5, 7, 6, 8], [1, 6, 2, 4]))