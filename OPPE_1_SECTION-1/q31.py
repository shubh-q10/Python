def are_orthogonal(t1: tuple, t2: tuple) -> bool:
    return ((t1[0]*t2[0] + t1[1]*t2[1]) == 0)


print(are_orthogonal((1, 0), (12, -6)))