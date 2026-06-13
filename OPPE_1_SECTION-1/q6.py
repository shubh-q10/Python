def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    mid = len(t) // 2
    mid_value = t[mid]
    return t[:mid] + (mid_value,)*n + t[mid + 1:]

print(replace_middle_with_n_times_middle((1, 2, 3, 4, 5), 40))
    
