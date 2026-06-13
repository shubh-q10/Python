def number_with_more_unique_digits(n1:int, n2:int):
    unique_in_n1 = set(str(n1))
    unique_in_n2 = set(str(n2))
    if len(unique_in_n1) < len(unique_in_n2):
        return n2
    elif len(unique_in_n1) > len(unique_in_n2):
        return n1
    else:
        return (n1, n2)
    
num = input()
num1 = input()
print(number_with_more_unique_digits(num, num1))
