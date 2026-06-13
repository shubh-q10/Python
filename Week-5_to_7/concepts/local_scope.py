def local_scope():
    s = "This is the local variable which can't be accessed outside of this function"
    print(s)

local_scope()
print(s) #this will show error coz s is not defined outside of function local_scope