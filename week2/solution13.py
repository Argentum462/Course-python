# Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами.
# Выведите одно из четырех слов: rectangular для прямоугольного треугольника,
# acute для остроугольного треугольника, obtuse для тупоугольного треугольника
# или impossible, если треугольника с такими сторонами не существует
# (считаем, что вырожденный треугольник тоже невозможен).
a = int(input())
b = int(input())
c = int(input())
if (a + b > c > abs(a - b)) or (a + c > b > abs(a - c)) \
        or (c + b > a > abs(c - b)):
    if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) \
            or (c ** 2 == b ** 2 + a ** 2):
        print('rectangular')
    elif (a ** 2 < b ** 2 + c ** 2) and (b ** 2 < a ** 2 + c ** 2) \
            and (c ** 2 < b ** 2 + a ** 2):
        print('acute')
    elif (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2) \
            or (c ** 2 > b ** 2 + a ** 2):
        print('obtuse')
    else:
        print('impossible')
else:
    print('impossible')
