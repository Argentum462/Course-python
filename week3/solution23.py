# Замена внутри фрагмента
s = input()
k1 = s.find("h")
k2 = s.rfind("h")
s1 = s[k1 + 1:k2]
print(s[:k1 + 1] + s1.replace('h', 'H') + s[k2:])
