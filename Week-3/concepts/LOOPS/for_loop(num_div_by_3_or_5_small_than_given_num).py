#FIND ALL POSITIVE NUMBERS DIVISIBLE BY 3 OR 5 WHICH ARE SMALLER THAN THE GIVEN NUMBER

def div_by_3(n):
    if n%3 == 0:
        return True
    else:
        return False

def div_by_5(n):
    if n%3 == 0:
        return True
    else:
        return False
    
    
num = int(input("enter the number here: "))
for i in range(1, num+1):
    if i < num and (div_by_3(i) or div_by_5(i)):
        print(i, end=",")
    
        