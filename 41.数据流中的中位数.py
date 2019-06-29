# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data=[]
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self,data):
        # write code here
        l=len(self.data)
        if l%2==0:
            return (self.data[l//2]+self.data[l//2-1])/2.0
        else:
            return self.data[l//2]
class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
    def Insert(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 维护两个堆,大根堆保存最小的1/2数据,小根堆保存最大的1/2数据
        # 两个堆的长度不超过1个
        # 注意: python中没有大根堆,用小根堆取负代替

        # Corner case:初始化
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
            return
        # 初始化的时候必须保证小根堆的数比大根堆的树要大
        if len(self.max_heap) == 0 and len(self.min_heap) == 1:
            if num > self.min_heap[0]:
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            return

        if len(self.min_heap) >= len(self.max_heap):
            if num < -self.max_heap[-1]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
        else:
            if num > self.min_heap[-1]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
                temp = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -temp)

    def GetMedian(self, n=None):
        # 注意取值的时候应该是heap[0]
        if len(self.min_heap) == len(self.max_heap):
            if len(self.min_heap) != 0:
                return float(self.min_heap[0] - self.max_heap[0]) / 2
            else:
                return None
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]