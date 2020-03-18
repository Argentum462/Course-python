def IsPointInSquare(x, y):
    return abs((x * y) / 2) <= x and abs((x * y) / 2) <= y


a, b = float(input()), float(input())
if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')