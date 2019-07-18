def Power(base, exponent):
    if base == 0 and exponent < 0:
        return 0
    # 否则0的-n次方会报错误
    if exponent < 1:
        return 1 / (getpower(base, -exponent))
    else:
        return getpower(base, exponent)


def getpower(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    res = 1
    for i in range(exponent):
        res *= base
    return res


def Power_digui(base, exponent):
    if base == 0 and exponent < 0:
        return 0
    # 否则0的-n次方会报错误
    if exponent < 1:
        return 1 / (getpower_digui(base, -exponent))
    else:
        return getpower_digui(base, exponent)


def getpower_digui(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    res = getpower_digui(base, exponent // 2)
    res *= res
    if exponent & 1==1:
    #如果exponent为奇数时 递归返回后说少乘以一个res的
        res=res*base
    return res


print(Power(2, 7))
print(Power_digui(2, 7))
