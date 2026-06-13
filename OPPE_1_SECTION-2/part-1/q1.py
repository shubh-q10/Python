def sum_of_squares_of_even(nums: list) -> int:
    sqr_sum = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            sqr_sum += nums[i]**2
    return sqr_sum

print(sum_of_squares_of_even([1, 2, 3, 4, 5, 6]))
