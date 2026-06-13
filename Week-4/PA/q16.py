# L = [(x, y) for x in range(1, 100) for y in range(1, 100) if x + y == 100]
# print(L)

# L = [ ]
# for x in range(1, 100):
#     for y in range(1, 100):
#         if x + y == 100:
#             L.append((x, y))
# print(L)

L = [(x, 100 - x) for x in range(1, 100)]
print(L)