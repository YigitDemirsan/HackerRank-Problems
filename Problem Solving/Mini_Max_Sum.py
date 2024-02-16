def miniMaxSum(arr0):
    min_sum = 0
    max_sum = 0
    count = 0
    count_1 = 0
    arr0.sort()

    for i in range(0, arr0.__len__()):
        if arr0.__len__() > 5 and count < 5:
            min_sum = min_sum + arr0[i]
            count = count + 1
        elif arr0.__len__() <= 5 and count < 4:
            min_sum = min_sum + arr0[i]
            count = count + 1

    b = arr0.copy()
    for i in b[::-1]:
        if b.__len__() > 5 and count_1 < 5:
            max_sum = max_sum + i
            count_1 = count_1 + 1
        elif b.__len__() <= 5 and count_1 < 4:
            max_sum = max_sum + i
            count_1 = count_1 + 1

    return print(str(min_sum) + " " + str(max_sum))
