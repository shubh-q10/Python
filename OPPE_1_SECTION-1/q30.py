def remove_n_elems_from_index(t: tuple, n: int, i: int) -> tuple:
    return t[:i] + t[i + n:]

print(remove_n_elems_from_index((1, 2, 3, 4, 5), 2, 1))
