def maxProduct(length):
    if length<2:
        return 0
    if length==2:
        return 1
    if length==3:
        return 2
    product=[0,1,2,3]#设置长度0123的长度
    for i in range(4,length+1):
        max=0
        for j in range(1,i//2+1):
            #分别计算f(i)*f(n-i)的最大值
            num=product[j]*product[i-j]
            if (num>max):
                max=num
        product.append(max)#获取长度为i时 可切割的最大值
    return product[-1]
print(maxProduct(4))


