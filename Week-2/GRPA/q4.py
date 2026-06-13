import math

operation = input().strip()

if operation == "odd_num_check":
    number = int(input().strip())
    print("yes" if number % 2 != 0 else "no")

elif operation == "perfect_square_check":
    number = int(input().strip())
    root = int(math.sqrt(number))
    print("yes" if root * root == number else "no")

elif operation == "vowel_check":
    text = input().strip().lower()
    print("yes" if any(ch in "aeiou" for ch in text) else "no")

elif operation == "divisibility_check":
    number = int(input().strip())
    if number % 2 == 0 and number % 3 == 0:
        print("divisible by 2 and 3")
    elif number % 2 == 0:
        print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    text = input().strip()
    print(text + text[-2::-1])   # mirror without repeating last char

elif operation == "simple_interest":
    principal_amount = int(input().strip())
    n_years = int(input().strip())
    rate = 5 if n_years < 10 else 8
    si = (principal_amount * rate * n_years) / 100
    print(round(si))

else:
    print("Invalid Operation")
