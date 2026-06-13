#REVERSE THE DIGITS OF THE GIVEN NUMBER

# num = int(input("Enter the number here: "))
# while num > 0:
#     digit = num % 10
#     num //= 10
#     print(digit, end="")

num = str(int(input("Enter the num here: ")))
rev_num = num[::-1]
print(int(rev_num))
    
