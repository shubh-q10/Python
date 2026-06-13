a, b, c, d = 5, 2, 3, 4
x = float(5.234)
print(int(x))
print(int(-x))
'''it means if we convert float to integer it will remove the decimal point numbers'''


'''Another method by using f string so we don't need to use number in decimal form'''

e, f, g, h = 10, 4, 6, 8
y = float(f"{e}.{f}{g}{h}") 
print(int(y))
print(int(-y))