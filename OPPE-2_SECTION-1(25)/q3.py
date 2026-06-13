l1 = [5, 6, 7, 8]
l2 = [1, 2, 6, 4]
elem = 6

def is_present_in_opposite_halves(elem, l1: list, l2: list):
    mid1 = len(l1) // 2
    mid2 = len(l2) // 2
    
    l1_first = l1[:mid1]
    l1_second = l1[mid1:]
    l2_first = l2[:mid2]
    l2_second = l2[mid2:]
    return ( (elem in l1_first and elem in l2_second) or ( elem in l1_second and elem in l2_first) )





print(is_present_in_opposite_halves(elem, l1, l2))