# Задача 2. В файле находятся названия фруктов.Выведите все фрукты, названия которых начинаются на заданную букву.
# а–>абрикос,авокадо, апельсин, айва.

data = open('fruits_list.txt', encoding= 'utf-8')
text = data.readlines()
data.close

letter = input('Задайте букву: ')
temp = []

for el in text:
    if el[0].casefold() == letter.casefold():
        temp.append(el)
print(f'{letter.upper()} -> {temp}')

