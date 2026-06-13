def is_odd_length_palindrome(s: str) -> bool:
    return((len(s) % 2 != 0) and (s == s[::-1]))
print(is_odd_length_palindrome("ili"))