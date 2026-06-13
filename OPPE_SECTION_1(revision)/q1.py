def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    sum_sq = a**2 + b**2
    abs_dff = abs((a**2) - (b**2))
    return ((sum_sq, abs_dff))

print(sum_squares_abs_diff_squares(4, 5))
