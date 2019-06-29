def Uguly(num):
    while num%2==0:
        num//=2
    while num%3==0:
        num//=3
    while num%5 ==0:
        num//=5
    return True if num==1 else False

def GetUgulyCount(index):
    count=0
    num=0
    while count<index:
        num+=1
        if Uguly(num):

            count+=1
    return num
print(GetUgulyCount(8))
def Uguly(num):
    while num%2==0:
        num//=2
    while num%3==0:
        num//=3
    while num%5 ==0:
        num//=5
    return True if num==1 else False

def GetUgulyCount(index):
    count=0
    num=0
    while count<index:
        num+=1
        if Uguly(num):

            count+=1
    return num
print(GetUgulyCount(8))