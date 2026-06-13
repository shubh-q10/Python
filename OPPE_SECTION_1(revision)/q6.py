def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    mid = len(t)//2
    return t[:mid] + t[mid:mid+1]*n + t[mid+1:]


print(replace_middle_with_n_times_middle((1, 2, 3, 5, 7), 5))
