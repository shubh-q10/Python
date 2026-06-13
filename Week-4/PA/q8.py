A = [[1, 2], [3, 4]]
B = A.copy()	# avoid this for matrices
A[0][0] = 100
print(A)
print(B)