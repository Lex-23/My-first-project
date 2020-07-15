m = 100
n = 105
m = min(m, n)
for i in range(m, n):
    for div in range(1, i-1):
        if i % div == 0:
            print(set(div))