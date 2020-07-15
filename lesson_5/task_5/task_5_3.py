for int_1 in range (200, 300):  # перебираем список по первому дружественному числу

    int_2 = 0  # второе дружественное число
    tmp = 0

    for div_1 in range (1, int_1):  # div_1 - делители первого числа
        if int_1 % div_1 == 0:
            int_2 += div_1

    for div_2 in range (1, int_2):  # div_2 - делители второго числа
        if int_2 % div_2 == 0:
            tmp += div_2

    if int_1 == tmp and int_1 != int_2 and int_1 < int_2:
        print(int_1, int_2)




