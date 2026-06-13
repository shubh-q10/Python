#The break statement is used to exit a loop prematurely, meaning it immediately ends 
# the closest for or while loop, regardless of the loop condition.


i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
    
#output 1, 2, 3, 4
