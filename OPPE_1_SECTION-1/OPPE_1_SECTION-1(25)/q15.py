nums = [1,2 ,3, 4, 6, 7, 8,9]
def find_missing_number(nums: list, n: int) -> int:
    for i in range(1,n+1):
        if i not in nums:
            return i
print(find_missing_number(nums, 9))