# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code
        if n<1 or m<1:
            return -1
        nuber=list(range(0,n))
        index=0
        while nuber:
            temp=nuber.pop(0)
            index+=1
            if index==m:
                index=0
                continue
            nuber.append(temp)
            if len(nuber)==1:
                return nuber[0]
                break

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        res = range(n)
        i = 0
        while len(res)>1:
            i = (m+i-1)%len(res)
            res.pop(i)
        return res[0]
a=Solution()
a.LastRemaining_Solution(5,3)
