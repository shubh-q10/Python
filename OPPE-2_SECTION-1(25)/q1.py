def is_even_two_digit_number(num):
    return (num % 2 == 0 and len(str(abs(num))) == 2)

print(is_even_two_digit_number(-56))
