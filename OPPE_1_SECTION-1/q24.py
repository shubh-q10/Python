def find_missing_number(nums: list, n: int) -> int:
    expected_sum = n*(n+1) // 2
    actual_sum = sum(set(nums))
    return expected_sum - actual_sum


print(find_missing_number([1, 4, 2, 4, 6, 5, 6], 6))
