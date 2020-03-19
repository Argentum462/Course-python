# Проверьте, принадлежит ли точка закрашенной области
def IsPointInCircle(x, y):
    a = (x + 1) ** 2 + (y - 1) ** 2 <= 4 and y >= -x and y >= 2 * x + 2
    b = (x + 1) ** 2 + (y - 1) ** 2 >= 4 and y <= -x and y <= 2 * x + 2
    return a or b


x, y = float(input()), float(input())
if IsPointInCircle(x, y):
    print('YES')
else:
    print('NO')
