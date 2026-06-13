D = {'a': 1, 'ab': 2, 'abc': 3, 'abcd': 4}

# easiest way to iterate through the keys of a dict
for key in D:
    value = D[key]
    print(f'{key}:{value}')