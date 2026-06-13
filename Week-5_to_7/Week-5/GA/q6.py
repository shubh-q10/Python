import random

nums = [ ]
for i in range(10000):
    nums.append(random.randint(1, 10))
    
    
def num_count(nums):
    d_count = {}
    for num in range(1, 11):
        d_count[num] = 0
    for num in nums:
        d_count[num] += 1
        
    return d_count

        

print(num_count(nums))