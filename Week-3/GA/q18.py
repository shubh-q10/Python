sentence = input()
value = ""
for char in sentence:
    if char in 'aeiou':
        value+=chr(ord(char)+1)
    else:
        value+=chr(ord(char)-1)
print(value)



'''

Pattern	Present?	Reason
Filtering	✅	The if statement filters behavior based on vowels.
Mapping	✅	Each character is transformed to a new character.
Aggregation	✅	All results are combined into a single string (value).

'''