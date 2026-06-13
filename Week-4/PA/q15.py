L = ['ono', 'two', 'strings', 'helmets']

P = []
for word in L:
    if word[0]==word[-1]:
        P.append(word)
        
print(P)