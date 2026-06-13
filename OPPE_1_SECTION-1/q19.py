def is_even_or_divisible_by_5(n:int) -> bool:
    if n % 2 == 0 or n % 5 == 0:
        return True
    else:
        return False

print(is_even_or_divisible_by_5(121))