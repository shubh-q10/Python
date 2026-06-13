n = int(input())
lines = [input() for _ in range(n)]
for i in range(0, n -1, 2):
    lines[i], lines[i + 1] = lines[i + 1], lines[i]

for i in range(n):
    if i % 2 == 0:
        lines[i] = lines[i][::-1]
        
for line in lines:
    print(line)