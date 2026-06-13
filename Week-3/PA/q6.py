#Using a while loop, determine the smallest positive integer x for which the expression x**2 + x + 41 is divisible by 41
x = 1
while True:
    if (x**2 + x + 41) % 41 == 0:
        print("Smallest x =", x)
        break
    x += 1

    
    