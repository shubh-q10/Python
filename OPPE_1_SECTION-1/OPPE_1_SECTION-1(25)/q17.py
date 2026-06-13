s = "name"
def upper_nth_index_char(s: str, n: int) -> str:
    if 0<= n <len(s):
        return s[:n] + s[n].upper() + s[n+1:]
    else:
        return s
print(upper_nth_index_char(s, 25))
