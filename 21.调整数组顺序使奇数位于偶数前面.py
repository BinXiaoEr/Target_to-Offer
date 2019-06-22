def ChangeNum(number):
    length = len(number)
    for i in range(length):
        if (number[i] % 2 != 0):
            num = number.pop(i)
            number.insert(0, num)
    return number


print(ChangeNum([6, 9, 25, 1, 2, 5, 8, 9, 6, 4, 7]))


def ChangeNum_New(number):
    lenth = len(number)
    first = 0
    last = lenth - 1
    while (first < last):
        while first < last and number[first] % 2 != 0:
            first += 1
        while first < last and number[last] % 2 == 0:
            last -= 1

        if first < last:
            number[first], number[last] = number[last], number[first]

    return number


print(ChangeNum_New([6, 9, 25, 1, 2, 5, 8, 9, 6, 4, 7]))
