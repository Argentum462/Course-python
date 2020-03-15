# Дублирование фрагмента
s = input()
k1 = s.find("h")
k2 = s.rfind("h")
s2 = s[k1 + 1:k2]
print(s[:k1 + 1] + s2 * 2 + s[k2:])
