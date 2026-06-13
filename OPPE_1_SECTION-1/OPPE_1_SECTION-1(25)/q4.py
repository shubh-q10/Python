def is_positive_odd_or_negative_even(n: int) -> bool:
    return (n % 2 != 0 and n > 0) or (n % 2 == 0 and n < 0)
print(is_positive_odd_or_negative_even(27))