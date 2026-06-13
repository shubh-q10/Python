import random

nums = [ ]
for i in range(10000):
    nums.append(random.randint(1, 10))
    
print(nums)

p = {}
for num in range(1, 11):
    p[num] = 0
for num in nums:
    p[num] += 1
    
print(p)

print(p[5]/10000)