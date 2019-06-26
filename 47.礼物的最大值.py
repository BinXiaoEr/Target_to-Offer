def getMaxValue_solution(values):
    rows=len(values)#行
    cols=len(values[0])#列
    #构造辅助二维数组
    maxValues=[[0]*cols]*rows
    for i in range(rows):
        for j in range(cols):
            left=0
            up=0
            if i>0:
                #获取上方的值
                up=maxValues[i-1][j]
            if j>0:
                #获取下方的值
                left=maxValues[i][j-1]
            #获取到达该值的最大
            maxValues[i][j]=max(up,left)+values[i][j]
    max_num=maxValues[rows-1][cols-1]
    return max_num
print(getMaxValue_solution([[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]))