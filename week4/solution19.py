# Дана последовательность чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.
def sum_nums():
    num = int(input())
    if num == 0:
        return num
    return num + sum_nums()


print(sum_nums())
