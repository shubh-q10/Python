# L = [(x, y) for x in range(1, 100) for y in range(1, 100) if x + y == 100 and x <= y]
# print(L)


L = [ ]
for x in range(1, 100):
    for y in range(1, 100):
        if x + y == 100 and x <= y:
            L.append((x, y))
            
print(L)