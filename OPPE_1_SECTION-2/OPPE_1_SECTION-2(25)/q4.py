n = int(input())
for _ in range(n):
    pairs = input().split(",")
    first = int(pairs[0])
    second = int(pairs[1])
    if _ % 2 == 0:
        print(first + second)
        
    else:
        print(abs(first - second))
        
        
    
        
