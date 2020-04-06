# Даны числа a, b, c, d, e. Подсчитайте количество таких целых
# чисел от 0 до 1000 (включительно), которые являются корнями уравнения
# (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество.
a, b = int(input()), int(input())
c, d, e = int(input()), int(input()), int(input())
k = 0
for i in range(1001):
    condition = (a * i**3 + b * i**2 + c * i + d)
    if i - e != 0 and condition / (i - e) == 0:
        k += 1
print(k)
