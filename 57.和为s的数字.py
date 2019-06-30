# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 1 or tsum is None:
            return []
        last = len(array) - 1
        first = 0
        num = None
        num1 = -1
        num2 = -1
        while first <last:
            sums = array[last] + array[first]
            if sums == tsum:
                b = array[first]
                a = array[last]
                if num is None or num > sums:
                    print(num)
                    num = sums
                    num1 = b
                    num2 = a
                last -= 1
                first += 1
            elif sums > tsum:
                last -= 1
            else:
                first += 1

        return [num1, num2] if num1!=-1 else []


a = Solution()
print(a.FindNumbersWithSum([1, 2, 3, 4, 5, 6], 7))
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        mid =(1+tsum)//2
        first=1
        last=2
        curnum=first+last
        result=[]
        while first<mid:
            if curnum==tsum:
                result.append([x for x in range(first,last+1)])
            while curnum>tsum and first<mid:
                #移除first的值
                curnum-=first
                #first后移动一格
                first+=1
                if curnum==tsum:
                    result.append([x for x in range(first, last + 1)])
            #如果值小了 则last往后移
            last+=1
            curnum+=last
        return result