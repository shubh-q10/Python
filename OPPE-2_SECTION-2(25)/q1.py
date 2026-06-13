nums = [101, -203, None, 99, 300]



def count_odd_three_digit_nums(nums):
    count = 0

    
    for x in nums:
        if (x is not None and x % 2 != 0) and (len(str(abs(x))) == 3):
            count += 1
    return count
        

print(count_odd_three_digit_nums(nums))        
    
    
    
    
