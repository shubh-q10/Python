l = [1, 2, 3, 0, -1, -7, None, 56, 21, 5]
def count_positive_ignore_none(nums: list):
    count = 0
    for num in l:
        if num == 0:
            continue
        elif num == None:
            continue
        elif num < 0:
            continue
        else:
            count += 1
    return count

print(count_positive_ignore_none(l))
    
