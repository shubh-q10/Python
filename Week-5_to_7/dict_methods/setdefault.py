dic = {0:"hello", 1:"world", 2:"welcome", 3:"to", 4:"programming"}
print(dic.setdefault(2)) #get the value of key 2
print(dic.setdefault("name", "shubham")) #making a new element in dic
print(dic.setdefault(5)) #None coz no key of 5 is present