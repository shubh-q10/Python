# A generator in Python is a special type of function that allows you to generate values lazily. 
# using the yield keyword instead of returning all values at once.


#SIMPLE

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


#ITERATING OVER THE GENERATOR

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
        
for _ in count_up_to(10):
    print(_)
    
    
#GENERATOR COMPREHENSION

gen_exp = (x * x for x in range(5))

for _ in gen_exp:
    print(_)
    
    
#ITERATOR FUNCTION

def power(limit):
    x = 0
    while x <= limit:
        yield x*x
        yield x*x*x
        x += 1

a = power(5)
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))

#OR WE CAN ITERATE OVER RANGE OF a

# for _ in a:
#     print(_)
