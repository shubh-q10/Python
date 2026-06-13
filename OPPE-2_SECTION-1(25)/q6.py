'''

Given two integers n1 and n2, return the number that contains more unique digits.

If both numbers have the same number of unique digits, return the both as a tuple as (n1, n2).

Assume both the integers n1 and n2 are positive integer.

Hint: Use set to find the unique digits, as sets automatically eliminate duplicates.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

n1 = 2345, n2 = 1111 -> 2345

Explanation

n1 = 2345 has the unique digits 2, 3, 4, 5 (4 unique digits).
n2 = 1111 has the unique digit 1 (1 unique digit).
Since n1 has more unique digits, the output is 2345.
Example

n1 = 1243, n2 = 123344 -> (1243, 123344)

Explanation

n1 = 1243 - 4 unique digits.
n2 = 123344 - 4 unique digits.
Since n1 has same number of unique digits, the output is (1243, 123344).


'''

def number_with_more_unique_digits(num1:int, num2:int):
    num1_set = {int(d) for d in str(num1)}
    num2_set = {int(d) for d in str(num2)}

    if len(num1_set) > len(num2_set):
        return (num1)
    elif len(num2_set) > len(num1_set):
        return (num2)
    elif len(num1_set) == len(num2_set):
        return ({num1}, {num2})
    
    
print(number_with_more_unique_digits(2345, 667787))
    

    