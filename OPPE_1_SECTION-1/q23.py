def is_rotation(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    return str2 in (str1 + str1)

print(is_rotation('abcde','cdeab'))