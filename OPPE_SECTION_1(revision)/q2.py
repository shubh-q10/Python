def is_odd_length_palindrome(s: str) -> bool:
    if len(s) % 2 != 0 and (s == s[::-1]):
        return True
    else:
        return False
    
print(is_odd_length_palindrome("heleh"))
print(is_odd_length_palindrome("hello"))
