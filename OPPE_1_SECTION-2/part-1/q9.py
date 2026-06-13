def replace_vowels_with_next_alphabet(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += chr(ord(char) + 1)
        else:
            result += char
    return result

print(replace_vowels_with_next_alphabet("artuidFGHIOa"))
            
