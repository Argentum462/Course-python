# Удалите из нее все символы, чьи индексы делятся на 3
s = input()
i = 0
s1 = ''
while i < len(s):
    if i % 3 == 0:
        s1 = s1 + ''
    else:
        s1 = s1 + s[i]
    i += 1
print(s1)
