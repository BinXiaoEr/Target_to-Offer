def CountOne(n):
    counts=[]
    if n<0:
        n=-n
    while n:
        a=n%2
        counts.insert(0,a)
        n=n//2
    return (counts.count(1))
def CountOne_yuyunsuan(n):
    count=0
    while n&0xffffffff !=0:#不进行此操作，n<0时会陷入无限循环
        #当长度超过32位或64位之后，Python3会自动将其转为长整型，长整型理论上没有长度限制。
        count+=1
        n=n&(n-1)
    return count
print(CountOne(9))
print(CountOne_yuyunsuan(9))