def div_by_exactly_one(num: int, a: int, b: int) -> bool:
    return (num % a == 0 or num % b == 0) and not(num % a == 0 and num % b == 0)

print(div_by_exactly_one(20, 3, 4))