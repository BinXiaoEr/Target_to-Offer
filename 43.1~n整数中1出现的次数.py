# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        counts=0
        for i in range(0,n+1):
            counts+=self.Numberone(i)

        return counts
    def Numberone(self,n):
        count=0
        while n:
            one=n%10
            if one ==1:
                count+=1
            n=n//10
        return count