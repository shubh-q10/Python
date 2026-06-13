def distance(x, y, metric = 'manhattan'):
    if metric == 'euclidean':
        return ((x**2 + y**2)**0.5)
    elif metric == 'manhattan':
        return (abs(x) + abs(y))
    
print(distance(45, 56))
        
    