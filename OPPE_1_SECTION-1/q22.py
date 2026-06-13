def is_both_divisible_by(a: int, b: int, c: int) -> bool:
    return a%c == 0 and b%c == 0
    
print(is_both_divisible_by(22, 20, 11))
