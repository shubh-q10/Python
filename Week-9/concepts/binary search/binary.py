#An efficient method to search the presence of an element in a sorted array.

num_list = [1, 3, 5, 7, 9]

def binary(num_list, target):
    low = 0
    high = len(num_list) - 1
    
    while 