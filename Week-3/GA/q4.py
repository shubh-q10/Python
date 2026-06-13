x = 0
x_ = 1
for i in range(10):
    x = x_
    x_ = x + x_
print(x)


x = 0
x_ = 1
for i in range(10):
    x, x_ = x_, x + x_
print(x)

