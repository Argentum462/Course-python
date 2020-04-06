# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
n = int(input())
sum_fact = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum_fact += factorial
print(sum_fact)
