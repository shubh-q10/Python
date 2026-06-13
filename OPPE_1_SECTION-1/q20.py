def deinterleave(s:str) -> str:
    char_at_even = s[::2]
    char_at_odd = s[1::2]

    return char_at_even + char_at_odd

print(deinterleave("abcdef"))
    