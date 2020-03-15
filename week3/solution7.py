# Определите размер вклада через K лет. Дробное число копеек по истечение
# года отбрасывается. Перерасчет суммы вклада (с отбрасыванием дробных частей копеек)
# происходит ежегодно.
P, X, Y = int(input()), int(input()), int(input())
K = int(input())
result = 0
sums = X * 100 + Y
while K > 0:
    result = int((sums * (P / 100)) + sums)
    sums = result
    K -= 1
print(result // 100, result % 100)
