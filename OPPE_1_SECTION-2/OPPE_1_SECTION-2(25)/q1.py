nums = [12, 1, 2, 9, 0]

def sum_of_squares_of_even(nums: list) -> int:
    sum = 0
    for x in nums:
        if x % 2 == 0:
            square = x*x
            sum = sum + square
    return sum
            





print(sum_of_squares_of_even(nums))
