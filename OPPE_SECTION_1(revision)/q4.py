def is_positive_odd_or_negative_even(n: int) -> bool:
    if (((n%2 != 0) and (n > 0)) or ((n%2 == 0) and (n<0)) ):
        return True
    else:
        return False
    
    
print(is_positive_odd_or_negative_even(0))
print(is_positive_odd_or_negative_even(3))
print(is_positive_odd_or_negative_even(-4))
print(is_positive_odd_or_negative_even(4))
print(is_positive_odd_or_negative_even(-3))









#either a positive odd number or a negative even number