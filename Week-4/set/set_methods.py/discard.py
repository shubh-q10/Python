# it also remove the element from the set but dont give error if element not found

set1 = {1, 2, 3, 34}
set2 = { 2, 4}

set1.discard(45) #don't give error if 45 is not in set1
print(set1)
set1.discard(34)
print(set1)