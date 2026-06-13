total = 0
count = 0
for i in range(1000):
    if i % 2 != 0 and count <= 50:
        total += i
        count += 1
    
    
average = total/count
print(average)
print(count)#to check how many first odd numbers
