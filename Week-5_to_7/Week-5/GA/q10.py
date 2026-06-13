nums = [1, 5, 5, 5, 5, 6, 6, 7, 5]


# if the number 5 occurs at least five times in a row


def streak(nums):
    if 5 not in nums:
        return False
    count = 0
    for num in nums:
        if num == 5:
            count += 1
            if count >= 5:
                return True
        else:
            count = 0
    return False
    
print(streak(nums))
    