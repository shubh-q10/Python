dic = {0:"hello", 1:"world", 2:"welcome", 3:"to", 4:"programming"}
print(dic.items()) #give the list containing a tuple for each key-value pairs
caot = 0
st = ""
for key, value in dic.items():
    caot += key
    st += value
    
print(caot, st)
    