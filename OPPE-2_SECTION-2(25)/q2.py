n = int(input())
name_list = [input() for _ in range(n)]
final = []
for name in name_list:
    parts = name.split(" ")
    initials = [p[0] + '.' for p in parts[:-1]]
    formatted = ' '.join(initials) + ' ' + parts[-1]
    final.append(formatted)
    
    
final.sort()
for name in final:
    print(name)
    

    