class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxindex= [0]     # 存放最大值，次大值下标的数组       
        res = []
        for i in range(len(nums)):
            # 判断下标对应的最大元素是否已经滑出窗口,即当前最大值的下标是不是在滑动窗口的范围内
            if i -maxindex[0] > k-1:
                maxindex.pop(0)

            # nums[i]与 maxindex 中的值比较，将小于nums[i]的值都弹出
            while (len(maxindex)>0 and nums[i] >= nums[maxindex[-1]]):
                maxindex.pop()
                # 如果maxindex的长度还没有达到最大规模
            if len(maxindex)< k-1:
                maxindex.append(i)
            if i >=k-1:     # 如果经过一个完整的窗口，保存当前的最大值
                res.append(nums[maxindex[0]])   #此行报错
        return res

class Solution(object):
    def maxInWindows(self, nums, k):
        maxnum=[0]#存储当前滑动窗口内的最大值的下标
        res=[]
        if k==1:
            return nums
        if k<=0:
            return []
        for i in range(len(nums)):
            #即当前m最大值的下标不在滑动窗口内 则要移除：
            if i-maxnum[0]>k-1:
                maxnum.pop(0)

            # nums[i]与 maxindex 中的值比较，将小于nums[i]的值都弹出
            while (len(maxnum) > 0 and nums[i] >= nums[maxnum[-1]]):
                maxnum.pop()
            #如果当前存储maxnum的范围小于窗口大小
            if len(maxnum)<k-1:
                maxnum.append(i)
            if i >= k - 1:  # 如果经过一个完整的窗口，保存当前的最大值
                #将当前maxnum头部的元素 作为下标存入res
                print(maxnum[0])
                res.append(nums[maxnum[0]])
        return res
a=Solution()
a.maxInWindows([2,3,4,2,6,2,5,1],1)