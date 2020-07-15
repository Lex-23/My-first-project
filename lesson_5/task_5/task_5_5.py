import random

list_1 = []
count = 0
while count < 19:
    n = random.randint(1, 100)  # генерация 19-ти случайных элементов для списка
    list_1.append(n)
    count += 1

print(f'list_1:\n{list_1}')
max_el = max(list_1)
print(f'max elem: {max_el}')

list_2 = []
for i in list_1:
    if list_1.index(i) % 2 != 0:
        list_2.append(i)
    else:
        list_2.append(max_el)

print(list_2)




