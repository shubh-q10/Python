def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for elem in s[::2]:
        if elem.isalpha():
            if elem in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return (vowel_count, consonant_count)

print(count_vowels_and_consonants_in_even_indices("abcde484djhjiis854dfkaeiou"))