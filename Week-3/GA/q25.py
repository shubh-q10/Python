for num in range(1000):  
    i = num
    result = 0
    while True:
        i -= 4
        if i>10:
            continue
        if i<-10:
            break
        result += i
    print(result)