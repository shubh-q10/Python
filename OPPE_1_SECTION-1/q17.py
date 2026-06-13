def is_divisible_by_last_two_digits(num: int):
    last_digit1 = int(str(num)[-1])
    last_digit2 = int(str(num)[-2])
        
    if last_digit1 == 0 or last_digit2 == 0:
        return False

    return num % last_digit1 == 0 and num % last_digit2 == 0
        
        
print(is_divisible_by_last_two_digits(44))
            
            
