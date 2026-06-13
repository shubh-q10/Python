P = [34, 32, 1, 2, 7, 8, 99]
Q, R = [],[]
for x in P:
    Q.append(-x)
Q.sort()
print(Q)
for x in Q:
    R.append(-x)
    
print(R)