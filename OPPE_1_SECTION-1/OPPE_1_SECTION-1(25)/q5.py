def within_and_has_double_quotes(s: str) -> bool:
    return (s[0], s[-1] == '"') and ('"' in s[1:-2]) 
print(within_and_has_double_quotes('"asnd"dfdf"'))