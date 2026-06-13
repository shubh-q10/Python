dic = {0:"hello", 1:{0:"Welcome", 1:"how", 2:"where"}, 2:"programming"}
print(dic[1][2]) #accessing the elements of nested dict
dic[1][2] = "when" #updating the elements of nested dict
print(dic)