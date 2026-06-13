s = "abcdefghi"
def deinterleave(s: str) -> str:
    return s[::2] + s[1::2]

print(deinterleave(s))
    
    