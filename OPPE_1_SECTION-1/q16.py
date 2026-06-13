def product_of_sum_and_abs_diff_of_digits(num: int):
    if len(str(num)) == 2:
        digits = str(num)
        sum = int(digits[0]) + int(digits[1])
        abs_diff = abs(int(digits[0]) - int(digits[1]))
        product_of_both = sum * abs_diff
        return (product_of_both)
    else:
        return "digits should be 2 only"

print(product_of_sum_and_abs_diff_of_digits(92))
