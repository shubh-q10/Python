#FIND THE MAX AMONG THE INPUT VALUES UNTIL -1

max_value = float('-inf')

while True:
    num = int(input("Enter -1 to stop this: "))
    if num == -1:
        break
    if num > max_value:
        max_value = num
print(f'The maximum value among the given numbers is: {max_value}')
    
# if max_value == float('-inf'):
#     print("no valid numbers were entered")
# else:
#     print(f'The maximum value entered is: {max_value}')


        



 