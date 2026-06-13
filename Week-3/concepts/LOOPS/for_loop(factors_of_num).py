#FIND THE FACTORS OF THE GIVEN NUMBER
fact_list = []
num = int(input("Enter the num here "))
for i in range(1, num+1):
    if num % i == 0:
        fact_list.append(i)
print(f'factors of {num} are {fact_list}')