A = [[1, 34, 45], [45, 51, 12]]
B = [[1, 34, 45], [45, 51, 12]]


def equality(A, B):
    if len(A) != len(B):
        return False
    if len(A[0]) != len(B[0]):
        return False
    
    m, n = len(A), len(A[0])
    
    is_equal = True
    for i in range(m):
        for j in range(n):
            if A[i][j] != B[i][j]:
                return False
                break
            
            if not is_equal:
                break
    return is_equal




def equality(A, B):
    if len(A) != len(B):
        return False
    if len(A[0]) != len(B[0]):
        return False
    
    m, n = len(A), len(A[0])
    
    for i in range(m):
        for j in range(n):
            if A[i][j] != B[i][j]:
                return False
    return True

print(equality(A, B))
                
            
    