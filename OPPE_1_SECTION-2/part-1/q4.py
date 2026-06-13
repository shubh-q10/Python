def count_odd_three_digit_nums(nums:list):
    count = 0
    for num in nums:
        if isinstance(num, int) and num % 2 != 0 and (99 < num <1000 or -99 > num > -1000):
            count += 1
            
    return count
    
    
print(count_odd_three_digit_nums([101, -203, None, 99, 300]))