import random

nums = [ ]
for i in range(10000):
    nums.append(random.randint(1, 10))
    
print(nums)
    
d_count = {}
for num in range(1, 11):
    d_count[num] = 0
for num in nums:
    d_count[num] += 1
        
print(d_count)

def check(d_count, N):
    S = 0
    for num in d_count:
        S += d_count[num]
    return S == N

print(check(d_count, len(nums)))


