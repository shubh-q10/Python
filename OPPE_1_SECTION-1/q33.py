def has_no_vowels_in_even_indices(s: str) -> bool:
    vowels = "aeiouAEIOU"
    for elem in s[::2]:
        if elem in vowels:
            return False
        
    return True
        
print(has_no_vowels_in_even_indices("hewox"))
