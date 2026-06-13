counti = 0
countj = 0
for i in range(10):
    for j in range(10):
        counti += 1
        break
    countj += 1
    break

print(counti, countj)