def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    middle_element = t[(len(t)//2)]
    return t[:(len(t)//2)] + (middle_element,) * n + t[(len(t)//2) + 1:]

print(replace_middle_with_n_times_middle((2,3,4,), 4))

