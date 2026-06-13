def merge_and_remove_duplicates(list1: list, list2: list) -> set:
    return set(list1 + list2)

print(merge_and_remove_duplicates(["ant", "bat"], ["bat", "cat"]))
