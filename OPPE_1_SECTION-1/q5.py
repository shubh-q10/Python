def within_and_has_double_quotes(s:str) -> bool:
    return s.startswith('"') and s.endswith('"') and s[1:-1].count('"') > 0
    
print(within_and_has_double_quotes('"hel"lo"'))
print(within_and_has_double_quotes(" heloo"))
    
