# M = [ [0 for j in range(3)] for i in range(3)]
# print(M)

M = [ ]
for i in range(3):
    M.append([ ])
    for j in range(3):
        M[-1].append(0)
        
print(M)