nums = [1, 2, 3, 4, 5, 6, 7, 8]
def sum_of_squares_of_even(nums: list) -> int:
    sum_sqs = 0
    for i in nums:
        if i % 2 == 0:
            sum_sqs += i**2
    return sum_sqs

print(sum_of_squares_of_even(nums))
            
    
