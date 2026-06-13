def increment_value_with_max_limit(d: dict, key: str, inc: int, limit: int):
    if key in d:
        d[key] = min(d[key] + inc, limit)
    else:
        d[key] = min(inc, limit)
    return d


    

