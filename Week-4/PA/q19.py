# n = int(input())
# L = []
# for i in range(n):
#     if i % 2 == 0:
#         L.append(1)
#     else:
#         L.append(0)
        
# print(L)


n = int(input())
L = [1 if x % 2 == 0 else 0 for x in range(n)]
print(L)