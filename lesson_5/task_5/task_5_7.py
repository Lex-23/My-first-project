import random

a = []
n = int(input(":"))

for i in range(n):
    vloj_spisok = []
    for j in range(n):
        vloj_spisok.append(random.randint(0, 9))
    a.append(vloj_spisok)
print(a)
for i in a:
    # print(max(i))
    for i, j in enumerate():
        print(j[i])


