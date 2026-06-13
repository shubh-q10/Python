def create_matrix(n):
    A = [ ]
    for i in range(n):
        row = [ ]
        for j in range(n):
            row.append(0)
        A.append(row)
    return A

print(create_matrix(3))