#FIND THE MULTIPLICATION TABLE OF THE GIVEN NUMBER

num = int(input("Enter the number here: "))
for i in range(1, 11):
    table = num*i
    print(f"{num} X {i} = {table}")