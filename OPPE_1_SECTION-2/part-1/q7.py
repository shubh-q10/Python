def count_unique_even_odd(l: list)-> dict:
    unique_num = set(l)
    even_count = sum(1 for num in unique_num if num % 2 == 0)
    odd_count = sum(1 for num in unique_num if num % 2 != 0)
    return {"even":even_count, "odd":odd_count}

print(count_unique_even_odd([1, 2, 2, 3, 4, 5, 5, 6, 9]))
