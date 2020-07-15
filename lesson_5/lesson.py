import random

a = []
n = int(input())
s = 0
for i in range(n):
    vloj_spisok = []
    for j in range(n):
        vloj_spisok.append(random.randint(0, 9))
        if j % 3 == 0:
            s += j
    a.append(vloj_spisok)
print(a)
print(s)

# n = 5
# m = 6
# a = []
# r = random.randint(0, 9)
# s = 0
# for i in range(n):
#     spisok = []
#     for j in range(m):
#         spisok.append(random.randint(0, 9))
#     a.append(spisok)





# for i in a:
#     for j in i:
#         if j == 7:
#             s += 1
# print(a)
# print(s)

# for i, elem in enumerate(['a', 'b', 'c', 'd']):
#     print(f'{i} - {elem}')

# a = []
# n = int(input())
# m = int(input())
# s = 0
# num = 0
# for i in range(n):
#     vloj_spisok = []
#     for j in range(m):
#         vloj_spisok.append(random.randint(0, 9))
#
#     a.append(vloj_spisok)
# print(a)
# for i in a:
#     for j in i:
#         s += j
# k = n * m
# sr = s / k
#
# for i in a:
#     for j in i:
#         if j > sr:
#             num += 1
# # for i in a:
# #     for j in i:

# print("num", num)
# print("sum", s)

# s = "abcd"
# print(s.startswith('a'))
# print(s.endswith("cd"))

pupils = [{"name": "Alice", "Num group": 42, "Phisics": 7, "Matem": 5,"Lung": 8,},
          {"name": "Ali", "Num group": 43, "Phisics": 2, "Matem": 6, "Lung": 1, "math": 1}]

for pupil in pupils:
    s = 0
    count = 0
    for key in pupil.keys():
        if key not in ["name", "Num group"]:
            s += pupil[key]
            count += 1
    if s/count > 4:
        print(pupil)

   





