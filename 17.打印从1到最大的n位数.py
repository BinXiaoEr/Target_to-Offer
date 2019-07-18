def PrintNum(n):
    nums=1
    for i in range(n):
        nums*=10
    for i in range(1,nums):
        print(i)

def Print(n):
    if n<=0:
        return
    list_num=['0']*n
    while Incre(list_num) is False:
        PrintNumber(list_num)

def PrintNumber(number):
    isBegin = False
    for i in range(len(number)):
        if number[i]!="0" and isBegin is False:
            isBegin = True
            if isBegin:
                tmp = ("".join(number[i:]))
                print(tmp)
                break


def Incre(number):
    isOverFlow=False
    isIn=0
    len_num=len(number)
    n=len_num-1
    while n>=0:
        #从最后一位开始而不是第一位
        nsum=int(number[n])+isIn
        if n==len_num-1:
            nsum+=1
        if nsum==10:
            if n==0:
                isOverFlow=True
                #当最后的一个99加1  就溢出 要返回
            else:
                isIn=1# 如果不是那么就前面一位加一,自己变为0
                number[n]='0'
        else:
            number[n]=str(nsum)
        n-=1
    return isOverFlow
#PrintNum(2)
#Print(2)


def PintCount_New(n):
    if n<=0:
        return None
    #n=3 则 0001 当第一个是1时结束输出 表示已经达到最大
    arr=[0]*(n+1)
    arr[n]=1
    while not arr[0]:
        print("".join(map(str,arr[1:])))
        #map它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
        i=n+1
        while i>1 and arr[i-1]==9:
            i-=1
        #判断当前从后往前有多少个9 如果连着9 则要前一位要加1且当前要清0最后1位继续加1  如果没有则最后1位继续加1
        arr[i-1]+=1
        #将获取到的连续9的位置重新至0
        for j in range(i, n + 1):
            arr[j] = 0
    return True
PintCount_New(2)