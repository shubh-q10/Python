def surround_first_two_and_last_two_with_brackets(s: str):
    first_two = s[:2]
    mid = s[2:-2]
    last_two = s[-2:]
    return (f"[{first_two}]{mid}[{last_two}]")

print(surround_first_two_and_last_two_with_brackets("hloji"))
