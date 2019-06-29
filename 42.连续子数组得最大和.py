# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array)==0:
            return 0
        counts=0
        max_nums= -2**7#设置一个整形最小值
        for i in range(len(array)):
            if counts<=0:
                counts=array[i]
            else:
                counts+=array[i]

            if counts>max_nums:
                max_nums=counts
        return max_nums