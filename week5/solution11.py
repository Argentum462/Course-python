# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
n = int(input())
cards1 = 0
cards2 = 0
for i in range(1, n):
    card = int(input())
    cards1 += card
    cards2 += i
print(cards2 + n - cards1)
