def is_even_and_second_last_digit_is_two(num: int) -> bool:
    return ((num % 2 == 0) and ((num // 10) % 10 == 2))