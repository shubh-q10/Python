def is_rotation(str1: str, str2: str) -> bool:
    return ((len(str1) == len(str2)) and (str1 in (str2 + str2)))