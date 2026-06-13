def upper_nth_index_char(s: str, n: int) -> str:
    if n > len(s):
        return s
    return s[:n] + s[n].capitalize() + s[n+1:]

        
    
print(upper_nth_index_char("hellohi", 4 ))