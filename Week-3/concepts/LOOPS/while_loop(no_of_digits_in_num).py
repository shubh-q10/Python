#FIND THE NO.OF DIGITS IN A NUMBER

num = int(input("Enter the number: "))
count = 0
while (num > 0):
    count += 1
    num //= 10
print(f"no of digits in the given number is {count}")

    