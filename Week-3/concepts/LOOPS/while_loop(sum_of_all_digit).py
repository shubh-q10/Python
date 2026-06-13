#FIND THE SUM OF ALL DIGITS IN THE NUMBER

# num = int(input("Enter the number: "))
# sum_digit = 0
# while num > 0:
#     sum_digit += num % 10
#     num //= 10
# print(sum_digit)


num = str(int(input("Enter the num here: ")))
sum = 0
for i in num:
    sum += int(i)
print(sum)
    