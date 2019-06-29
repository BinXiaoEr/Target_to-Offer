class Solution:
    def __init__(self):
        self.reslut=[]
    def Vlue(self,num):
        lists=[str(x) for x in num]
        self.GetPath(lists,0)
       # return min(self.reslut)
        return self.reslut
    def GetPath(self,num,begin):
        if begin==len(num)-1:

            self.reslut.append(int("".join(num[:])))
        for i in range(begin,len(num)):
            if num[begin]==num[i] and begin!=i:
                continue
            else:
                num[begin],num[i]=num[i],num[begin]
                self.GetPath(num,begin+1)
                num[begin], num[i] = num[i], num[begin]
# -*- coding:utf-8 -*-
class Solutions:
    def __init__(self):
        self.reslut=[]
    def PrintMinNumber(self,num):
        if not num:
            return ""
        lists=[str(x) for x in num]
        self.GetPath(lists,0)
        return min(self.reslut)
    def GetPath(self,num,begin):
        if begin==len(num)-1:

            self.reslut.append(int("".join(num[:])))
        for i in range(begin,len(num)):
            if num[begin]==num[i] and begin!=i:
                continue
            else:
                num[begin],num[i]=num[i],num[begin]
                self.GetPath(num,begin+1)
                num[begin], num[i] = num[i], num[begin]

class Solution:
    def theMax(self, str1, str2):
        '''定义字符串比较函数'''
        return str1 if str1+str2 > str2+str1 else str2

    def PrintMinNumber(self, numbers):
        """使用冒泡进行排序(把最大的放最后)"""
        string = [str(num) for num in numbers]
        res = []
        flag = True#用于判断已经是递增的则直接可以输出 减少不必要的是时间浪费
        count = len(string) - 1
        while flag and  count > 0:
            flag = False
            for i in range(len(string)-1):
                if self.theMax(string[i], string[i+1]) == string[i]:
                    temp = string[i]
                    del string[i]
                    string.insert(i+1, temp)
                    flag = True
            count -= 1
        string = ''.join(string)
        return string
a=Solution()

print(a.Vlue([1,1,2,3,3,4]))