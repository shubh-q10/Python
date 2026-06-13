'''
Write a function count_unique_even_odd that takes list of integers, returns a dictionary with the count of unique even and odd numbers in the list.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

>>> l = [1, 2, 2, 3, 4, 5, 5, 6, 9]
>>> count_unique_even_odd(l)
{"even": 3, "odd": 4}
Explanation

unique even numbers are 2,4 and 6 and their count is 3
unique odd numbers are 1,3,5 and 9 and their count is 4
'''
l = [1, 2, 2, 3, 4, 5, 5, 6, 9]

def count_unique_even_odd(l: list)-> dict:
    result = dict()
    count_odd = 0
    count_even = 0
    for i in set(l):
        if i%2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    result["even"] = count_even
    result["odd"] = count_odd
    return result
            
            
        
    print(count_i)
    
    
    


print(count_unique_even_odd(l))
    
