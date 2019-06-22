
def Circle(numbers,columns,rows):
    if numbers==None or columns<0 or rows<0:
        return
    statr=0
    #因为一圈的起始位置都是在(0,0),(1,1),(2,2)
    while columns>statr and rows>statr*2:
        PrintCirlcle(numbers,columns,rows,statr)
        statr+=1
def PrintCirlcle(numbers,columns,rows,start):
    #当前需要循环的 行和列范围
    endX=columns-1-start#列
    endY=rows-1-start#行
    #从左到右打印
    for i in range(start,endX+1):
        print(numbers[start][i])
    #从上到下 如果没有从上到下要进行判断
    if start<endY:
        for i in range(start+1,endY+1):
            print(numbers[i][endX])
    #从右到左
    if (start<endX and start<endY):
        for i in range(endX-1,start-1,-1):
            print(numbers[endY][i])

    #从下到上
    if start<endX and start<endY-1:
        for i in range(endY-1,start,-1):
            print(numbers[i][start])

test=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],

]
Circle(test,4,3)