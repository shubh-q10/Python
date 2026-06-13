def within_and_has_double_quotes(s: str) -> bool:
    return ((s[0] == '"' and s[-1] == '"') and '"' in s[0:-1])


print(within_and_has_double_quotes( '"abcd"efgh"'))
