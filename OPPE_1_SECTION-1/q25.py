def is_even_and_second_last_digit_is_two(num:int) -> bool:
    return (num % 2 == 0 and int(str(num)[-2]) == 2)

print(is_even_and_second_last_digit_is_two(254))




    
    