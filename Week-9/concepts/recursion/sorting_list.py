L = [34, 4, 23, 21, 55, 89, 100]


def recursion_sort(L):
    if L == []:
        return L
    mini = min(L)
    L.remove(mini)
    return [mini] + recursion_sort(L)

print(recursion_sort(L))


