# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        number = 0
        length = len(data)
        if len(data)>0:
            first = self.Get_First(data,k, length, 0, length - 1)
            last = self.Get_Last(data,k, length, 0, length - 1)
            if first>-1 and last>-1:
                number=last-first+1
            print(first)
            print(last)
        return number
    #找第一个
    def Get_First(self, data, k,lenth, start, end):
        if start>end:
            return -1
        mid=(end+start)//2
        mid_num=data[mid]
        if mid_num==k:
            #当两个值相同时，如果是前面的数不相同则表明该是起点位置或者指标等于0也是起点
            if (mid>0 and data[mid-1]!=k) or mid==0:
                return mid
            else:
                end=mid-1
        #如果中间值比k大 说明在左半部分
        elif mid_num>k:
            end=mid-1
        else:
            start=mid+1
        return self.Get_First(data,k,lenth,start,end)


    #找最后一个
    def Get_Last(self, data,k, lenth, start, end):
        if start > end:
            return -1
        mid = (end +start) // 2
        mid_num = data[mid]
        if mid_num == k:
            # 当两个值相同时，如果是后面的数不相同则表明该是终点位置或者指标等于最后一个值也是终点
            if (mid <lenth-1 and data[mid + 1] != k) or mid == lenth-1:
                return mid
            else:
                start = mid + 1
        # 如果中间值比k大 说明在左半部分
        elif mid_num <k:
            start = mid + 1
        else:
            end = mid - 1
        return self.Get_Last(data, k, lenth, start, end)
a=Solution()
a.GetNumberOfK([1,2,2,3,3,3,4],3)