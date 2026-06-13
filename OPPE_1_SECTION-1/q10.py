def is_even_two_digit_number(n:int):
    return 10 <= abs(n) <= 99 and n % 2 == 0
print(is_even_two_digit_number(900))