#FIND THE FACTORIAL OF THE GIVEN NUMBER
num = int(input("Enter the num here "))
factorial = 1
for i in range(1, num+1):
    if num == 0:
        factorial = 1
    else:
        factorial = factorial*i
print(f'factorial of {num} is {factorial}')