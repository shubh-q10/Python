import random

nums = [ ]
for i in range(10000):
    nums.append(random.randint(1, 10))
    
print(nums)

P = {}
for num in range(1, 11):
    P[num] = 0
for num in nums:
    P[num] += 1
    
print(P)


def most_freq(P):
    freq_num, freq = 1, P[1]
    for num in range(1, 11):
        if P[num] > freq:
            freq_num, freq = num, P[num]
    return freq_num

print(most_freq(P))
        