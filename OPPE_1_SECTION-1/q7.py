def div_by_exactly_one(num:int, a:int, b:int) -> bool:
    is_div_by_a = num % a == 0
    is_div_by_b = num % b == 0
    return (is_div_by_a or is_div_by_b) and not(is_div_by_a and is_div_by_b)
    
print(div_by_exactly_one(34, 2, 4))
print(div_by_exactly_one(11, 7, 8))
print(div_by_exactly_one(50, 5, 10))