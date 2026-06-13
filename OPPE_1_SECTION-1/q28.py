def is_obtuse(theta_1: int, theta_2: int) -> bool:
    theta_3 = 180 - (theta_1 + theta_2)
    return theta_1 > 90 or theta_2 > 90 or theta_3 > 90

print(is_obtuse(56, 20))