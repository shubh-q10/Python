lst = [1, 2, 34, True, 00, 45] #True is treated as 1 in python and False is 0
lst.sort(reverse = True)
print(lst)#if reverse == True then descending order
lst.sort(reverse= False)
print(lst)#if reverse == False then ascending order
lst.sort()
print(lst)