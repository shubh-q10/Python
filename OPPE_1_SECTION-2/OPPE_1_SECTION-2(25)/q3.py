nums = [1, -2, 3, 0, None, 4]
count = 0
for num in nums:
    if num is not None and num > 0:
        count += 1
print(count)
    