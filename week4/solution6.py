# Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r
def IsPointInCircle(x, y, xc, yc, r):
    return (y - yc) ** 2 + (x - xc) ** 2 <= r ** 2


x, y = float(input()), float(input())
xc, yc = float(input()), float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
