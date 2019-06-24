# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss is None:
            return
        charlist = list(ss)
        result = []
        self.printNum(charlist, 0, result)
        result = ["".join(result[i]) for i in range(len(result))]
        result.sort()
        return result
    def printNum(self,ss, begin, result):
        if begin == len(ss) - 1:
            result.append(ss[:])
        # 从当前位置 改变其后面的字符顺序 实现递归
        for i in range(begin, len(ss)):
            # 如果字符串中出现两个重复的数字 则跳过 不然会出现两个一样的排序
            if ss[begin] == ss[i] and begin != i:
                continue
            else:
                ss[begin], ss[i] = ss[i], ss[begin]
                self.printNum(ss,0 + 1, result)
                # 回到上一个状态 让其继续保持前一个数字不变 改变后面两个数字的递归
                ss[begin], ss[i] = ss[i], ss[begin]



#问题二 求字符的所有组合
#abc 组合 a b c ab ac bc abc
# -*- coding:utf-8 -*-
class Solutions:
    def Permutation(self, ss):
        # write code here
        if ss is None:
            return
        charlist = list(ss)
        result = []
        test=[]
        self.printNum(charlist, 0, test,result)
        result = ["".join(result[i]) for i in range(len(result))]
        result.sort()
        return result
    def printNum(self,ss, begin,test, result):
        if len(test):
            result.append(test[:])
        for i in range(begin,len(ss)):
            if ss[begin] == ss[i] and begin != i:
                #要判断后面的数字和开始的数字是否要相同 如果后面的数字和开始的相同 则要跳过
                continue
            else:
                # 情况一：子集包含元素nbums[i]
                test.append(ss[i])
                #因为已经解决了第i个元素，需要递归从第i + 1个元素开始求解
                self.printNum(ss,i+1,test,result)
                #情况二:子集不包含nums[i]，即略过第i个元素 完全从下一个元素开始
                test.pop(-1)

a=Solution()
print(a.Permutation('aab'))

