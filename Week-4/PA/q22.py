
def is_prime(x):
    if x <= 1:
        return False 
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# P = dict()
# for x in range(2, 101):
#     P[x] = is_prime(x)

P = {x: is_prime(x) for x in range(2, 101)}
print(P)