def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    sum_of_square = (a**2) + (b**2)
    abs_diff_sqr = abs((a**2) - (b**2))
    return (sum_of_square, abs_diff_sqr)

print(sum_squares_abs_diff_squares(4, 5))
    