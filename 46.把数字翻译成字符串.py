class Solution:
    def GetTranslationCount(self, number):
        if len(number)<=0:
            return 0
        Snumber=str(number)
        length=len(Snumber)
        count=0
        counts=[0]*length
        #f(i)=f(i+1)+g(i,i+1)*f(i+2)
        # 第i位和第i+1位 两位数字拼接奇爱的数字在10-25范围内，函数g(i,i+1)位1否则位0
        for i in range(length-1,-1,1):
            count=0
            #用于判断当前数字是不是最后一个末尾数字 是的话当前要从1开始计算
            #因为如果是当前最后一个数他没右后面的数字跟他组合
            if i<length-1:#从当前i开始翻译包含从i+1开始的翻译的种树
                count=counts[i+1]
            else:#从末尾开始翻译只有一种
                count=1

            if i<length-1:
                #如果它后面还有数字
                t1=int(Snumber[i])
                t2=int(Snumber[i+1])
                nums=t1*10+t2
                #判断i和i+1位置上的整数拼接起来是否满足翻译的要求
                if nums>=10 and nums<=25:
                    if i<length-2:
                        #当满足要求时 且不是倒数第二个 则i位置上的包含了i+2开始翻译的种树
                        count+=counts[i+2]
                    else:
                        #从倒数第二个开始翻译时，只能+1
                        count+=1
            counts[i]=count
        return count





