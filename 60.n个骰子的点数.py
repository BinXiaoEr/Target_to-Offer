def offer60(n):
    # 第n个骰子得到k的次数由n-1个骰子 k-1 ~ k-6 的个数和所决定，动规递推式
    # f(n,k) = f(n-1,k-1) + f(n-1,k-2) + f(n-1,k-3)+ f(n-1,k-4)+ f(n-1,k-5)+ f(n-1,k-6)
    if n < 0:
        return
    number = [1 for _ in range(6)]
    total = 6 ** n
    for _ in range(2, n + 1):
        tmp = [number[0]]
        for i in range(1, len(number)):  # 这样的处理方式避免重复运算
            if i - 6 < 0:
                tmp.append(tmp[-1] + number[i])
            else:
                tmp.append(tmp[-1] - number[i - 6] + number[i])
        new = [number[-1]]  # 随着骰子数增多，每次多5种结果
        for i in range(-2, -6, -1):
            new.insert(0, new[i + 1] + number[i])
        # new = [(sum(number[-i:])) for i in range(5, 0, -1)]   这种处理冗余计算
        number = tmp + new
    return [i / total for i in number]


print(offer60(2))
