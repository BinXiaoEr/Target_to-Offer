def Get_K(nums,k):
    Quick_sort(nums,0,len(nums)-1)
    return nums[:k]
def Quick_sort(nums,first,last):
    low=first
    high=last
    mid_value = nums[low]
    if first>=last:
        return
    while low<high:
        while low<high and nums[high]>mid_value:
            high-=1
        #当high小于mid时就要将high值放入low处
        nums[low]=nums[high]
        while low<high and nums[low]<mid_value:
            low+=1
        #当low大于high时
        nums[high]=nums[low]
    #退出循环时 low=heigh d
    nums[low]=mid_value
    print(nums)
    Quick_sort(nums,first,low-1)
    Quick_sort(nums,low+1,last)

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(tinput) or len(tinput)==0:
            return []
        # write code here
        self.Quick_sort(tinput, 0, len(tinput)-1)
        return tinput[:k]

    def Quick_sort(self,nums, first, last):
        low = first
        high = last
        mid_value = nums[low]
        if first >= last:
            return
        while low < high:
            while low < high and nums[high] >= mid_value:
                high -= 1
            # 当high小于mid时就要将high值放入low处
            nums[low] = nums[high]
            while low < high and nums[low] < mid_value:
                low += 1
            # 当low大于high时
            nums[high] = nums[low]
        # 退出循环时 low=heigh d
        nums[low] = mid_value

        self.Quick_sort(nums, first, low - 1)
        self.Quick_sort(nums, low + 1, last)

    def GetLeastNumbers_Solution_New(self, tinput, k):
        if k > len(tinput) or len(tinput) == 0 or k==0:
            return []
        reslut=[]
        for i in range(len(tinput)):
            if len(reslut)<k:
                reslut.append(tinput[i])
            else:
                reslut.sort()
                num=reslut[-1]
                if num>=tinput[i]:
                    reslut[-1]=tinput[i]
        reslut.sort()
        return reslut

alist = [54,26,93,17,77,31,44,55,20]
alist.sort()
print(alist)
a=Solution()
print(a.GetLeastNumbers_Solution_New([4,5,1,6,2,7,3,8],4))

