x = int(input("Enter any number: "))
while(x % 5 != 0 and x % 10 != 0):
    x = int(input("Enter any number: "))
print("outside loop, the value of x is ", x)