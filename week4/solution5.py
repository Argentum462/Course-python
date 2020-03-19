# Даны два действительных числа x и y. Проверьте, принадлежит ли точка
# с координатами (x,y) заштрихованному ромбу (-1:1).
def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


a, b = float(input()), float(input())
if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')
