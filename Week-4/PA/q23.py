P = [23, 'hello', 'world', 5, 6, 78]
def copy(P):
    Q = []
    for elem in P:
        Q = Q + [elem]
    return Q

print(copy(P))