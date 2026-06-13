# #FIND WETHER THE GIVEN NUMBER IS PALINDROME OR NOT
# s = str(input("Enter the string here: "))
# left, right = 0, len(s)-1
# while left < right:
#     if s[left] != s[right]:
#         print("Not palindrome")
#     else:
#         print(s, "is palindrome")
#     left += 1
#     right -= 1
    
n = str(int(input("Enter the number here: ")))
print(n == n[::-1])
    
    


#use slicing instead of while loop to check palindrome

# def is_palindrome(st:str)->bool:
#     return st == st[::-1]  
    

# strings = str(input("Enter the string here: "))
# if is_palindrome(strings):
#     print(f"{strings} is the palindrome")
# else:
#     print(f"{strings} is not palindrome")
    
