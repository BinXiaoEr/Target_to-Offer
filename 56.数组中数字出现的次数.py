# 方法二：根据异或运算的特点，相同的数字经过异或运算后结果为0，
# 除单独出现一次的数字外，其他数字都是出现两次的，
# 那么这些数字经过异或运算后结果一定是0。
# 而任何数字与0进行异或运算都是该数字本身。
# 所以对数组所有元素进行异或运算，运算结果就是题目的答案。

class Solution:
    def singleNumber(self, nums):
        q=0
        for num in nums:
            q=q^num
            print(q)
        return q

a=Solution()
a.singleNumber([2,4,3,6,3,4,2])


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        #获取当前数组的异或结果
        resultExOr = self.ExOr(array)
        i = 0
        #右移 获取第一个出现1的位置
        while resultExOr and i <= 32:
            i += 1
            resultExOr = resultExOr >> 1
        num1, num2 = [], []
        for num in array:
            #如果当前数字的第i位是1 则放入数组num1 不是则放入num2
            if self.bitIs1(num, i):
                num1.append(num)
            else:
                num2.append(num)
        first = self.ExOr(num1)
        second = self.ExOr(num2)
        return [first, second]

    def ExOr(self, aList):
        ExOrNum = 0
        for i in aList:
            ExOrNum = ExOrNum ^ i
        return ExOrNum

    def bitIs1(self, n, i):
        n = n >> (i - 1)
        return n & 1

print(5>>1)