

def modify_global():
    global s  #by using global keyword we can modify global scope inside function
    s = "I don't love python"  
    print(s)
    
s = "I love python"
    
modify_global() #here s value changed to "I don't love python"
print(s) #here s also changed to "I don't love python"