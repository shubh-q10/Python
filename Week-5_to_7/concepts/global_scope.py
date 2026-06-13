s = "i love your car"

def global_scope():
    print(s)
    
    
global_scope() #This will not show error coz s is global scope variable so we can use it anywhere or any function