# Дана последовательность целых чисел, заканчивающаяся числом 0.
# Выведите эту последовательность в обратном порядке.
def revers():
    num = int(input())
    if num == 0:
        return print(num)
    revers()
    print(num)


revers()
