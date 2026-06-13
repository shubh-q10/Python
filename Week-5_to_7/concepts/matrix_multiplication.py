def matrix_mul(x, y):
    r1, c1 = len(x), len(x[0])
    r2, c2 = len(y), len(y[0])
    result = 0
    
    if c1 != r2:
        raise ValueError("Number of columns in x must be equal to rows in y")
    
    result = [[0]*c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += x[i][k] * y[k][j]
    return result

A = [[1, 2, 3], [23, 34, 56]]
B = [[23, 34, 11], [11, 22, 10], [1, 2, 3]]
c = matrix_mul(A, B)
for row in c:
    print(row)
        