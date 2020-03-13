# Последовательность состоит из целых чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.
num = int(input())
max_num = num
while num != 0:
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)
