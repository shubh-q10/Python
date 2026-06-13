def first():
    second()
    print('first')

def second():
    third()
    print('second')

def third():
    print('third')
    
first()

