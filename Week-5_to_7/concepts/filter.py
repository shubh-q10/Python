# The filter() function in Python is used to filter elements from an iterable (list, tuple, set, etc.). 
# based on a condition.

#EXAMPLE-1

numbers = [1, 2, 3, 4, 5]
even_number = list(filter(lambda x: x%2 == 0, numbers))
print(even_number)

#USING LIST COMPREHENSION
num = [56, 67, 89, 34, 12, 2, 3, 0]
print("This list is make by one-liner list comprehension", [x for x in num if x%2 == 0])


#EXAMPLE-2

def is_even(n):
    return n%2 == 0

nums = [45, 67, 89, 34, 56, 78, 0, -12, 34, 33, 55, 43, 21]
even_numbers = list(filter(is_even, nums))
print("Using filter inside named functions", even_numbers)


#EXAMPLE-3, FILTERING STRINGS

words = ["hi", "shub", "elephant", "tiger", "wow", "ji",  "honey"]
long_words = list(filter(lambda x: len(x)>3, words))
print("List of words greater than 3", long_words)


#USING FUNCTION
def is_more_3(x):
    return len(x) > 3
long = list(filter(is_more_3, words))
print("List of words greater than 3 using function", long)

