# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers)<1:
            return False
        numbers.sort()
        num_zero=0
        for i in numbers:
            if i == 0:
                num_zero+=1
       # print(num_zero)
        num_need_zero=0
        start=num_zero#从第n个位置不是0的开始
        end=start+1
        while end<len(numbers):
            if numbers[start]==numbers[end]:
                #如果出现两个相同的数字 则一定不会是对子
                return False
            num_need_zero+=numbers[end]-numbers[start]-1#获取相邻两个数中间的间隔
            start=end
            end+=1
       # print(num_need_zero)
        return True if num_need_zero<=num_zero else False



a=Solution()
print(a.IsContinuous([0,3,1,6,4]))