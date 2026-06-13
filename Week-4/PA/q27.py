'''

if you two function with same name then only the last function will be executed

'''

def some_math_function(x):
    return x ** 2

def some_math_function(x):
    return x ** 3

print(some_math_function(2))