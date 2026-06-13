total = 0
for i in range(1, 5):
    print(i)
    for j in range(i):
        total += i #here we adding i not j so (1) + (2 + 2) + ( 3 + 3 + 3) + (4 + 4 + 4 + 4)
        print(j)
print(total)