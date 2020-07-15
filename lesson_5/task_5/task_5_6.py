import random

list_1 = [random.randint(0, 500) for el in range(30)]
print(f'list_1:\n{list_1}')


count = 0  # счетчик участков роста
for i, el in enumerate(list_1):
    if i == (len(list_1) - 1):
        break
    if el < list_1[i+1] and el < list_1[i-1]:
        count += 1
print(f'count area of rice: {count}')



