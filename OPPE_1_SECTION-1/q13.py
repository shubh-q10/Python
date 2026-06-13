def sum_of_floored_to_tens(a:int, b:int):
    a_floored = round(a//10)*10
    b_floored = round(b//10)*10
    floor_sum = a_floored + b_floored
    return floor_sum

print(sum_of_floored_to_tens(34, 46))
