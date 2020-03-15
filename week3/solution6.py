# Процентная ставка по вкладу составляет P процентов годовых, которые
# прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
# Определите размер вклада через год.
P, X, Y = int(input()), int(input()), int(input())
# Плохой способ
sums = X + (Y / 100)
result = (sums * (P / 100)) + sums
floats = round(result - int(result), 4)
print(int(result), int(floats * 100))
# Хороший способ
sums = X * 100 + Y
result = int(sums + (sums * (P / 100)))
print(result // 100, result % 100)
