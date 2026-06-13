bool_var = True
x = int(900)

if bool_var:
    x = x + 1
    bool_var = not bool_var
    if bool_var:
        x = x + 1
        print("Line 5 executed") # LINE-5 IS NEVER EXECUTED FOR TRUE OR FALSE 
    else:
        x = x - 1
print(x)

'''No matter if bool-var is True or False value of variable x is independent of value of variable bool_var '''
"""line-5 will never be executed coz at that time bool_var will always be False"""
