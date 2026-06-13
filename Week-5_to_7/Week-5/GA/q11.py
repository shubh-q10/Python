points = [(1, 1), (1, 2), (1, 3), (1, 4), (0, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1)]

def color_it(points):
    coloured_points = dict()
    for point in points:
        x, y = point
        if x + y == 4:
            coloured_points[point] = 'red'
        elif x + y > 4:
            coloured_points[point] = 'yellow'
        elif x + y < 4:
            coloured_points[point] = 'green'
    return coloured_points

print(color_it(points))
            