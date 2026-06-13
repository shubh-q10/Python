l = [1, 1, 3, 4, 5, 6, 8, 2, 3, 4]
def count_unique_even_odd(l: list)-> dict:
    even_c = 0
    odd_c = 0
    unique_l = list(set(l))
    for i in unique_l:
        if i % 2 == 0:
            even_c += 1
        else:
            odd_c += 1
    return {"even":even_c, "odd":odd_c}

print(count_unique_even_odd(l))
            
