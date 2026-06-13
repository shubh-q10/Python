def is_positive_odd_or_negative_even(n:int):
    if ((n%2 != 0) and n > 0) or ((n%2 == 0) and n < 0):
        return True
    else: 
        return False
    
print(is_positive_odd_or_negative_even(56))