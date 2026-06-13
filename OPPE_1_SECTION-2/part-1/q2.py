def count_positive_ignore_none(nums: list):
    count = 0
    for i in nums:
        if i is not None and i > 0:
            count += 1
        
    return count
            
            
print(count_positive_ignore_none([1, 2, -12, 0 , None, 22, 34]))