# pos = 1
# letters = 'abcdefghijklmnopqrstuvwxyz'
# letters_map = {}

# for letter in letters:
#     letters_map[letter] = pos
#     pos +=1
    
# print(letters_map)




# letters = 'abcdefghijklmnopqrstuvwxyz'
# letters_map = dict()

# for letter in letters:
#     letters_map[letter] = letters.index(letter) + 1
# print(letters_map)



letters = 'abcdefghijklmnopqrstuvwxyz'
letters_map = dict()

for i in range(len(letters)):
    letter = letters[i]
    letters_map[letter] = i + 1
    
print(letters_map)