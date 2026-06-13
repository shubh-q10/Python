d = {'x': 2, 'y': 7, 'z': 4}

def increment_value_with_max_limit(d: dict, key: str, inc: int, limit: int):
    d[key] += inc
    d[key] = min(d[key], limit)
    return d
    
        
print(increment_value_with_max_limit(d, 'y', 4, 10))
