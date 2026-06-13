#THE MAP FUNCTION IN PYTHON IS USED TO APPLY A FUNCTION TO EVERY ITEM IN AN ITERABLE(list, tuple, etc) WITHOUT USING LOOP


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#using list comprehensions 
print([x**2 for x in numbers])


#USING MAP INSIDE A FUNCTION

def square(n):
    return n**2

num = (1, 2, 3, 4, 5)
result = map(square, num)
print(result)
print(set(result))


#USING LAMBDA FUNCTION IN MAP
negnum = [-1, -2, -3, -4, -5]
print("LIST OF SQUARE OF NEGATIVE NUMBERS", list(map(lambda x: x**2, negnum)))