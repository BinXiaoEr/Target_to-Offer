def ReverNum(nums):
    length=len(nums)
    result=[]
    for i in range(length):
        first=nums[i]
        for j in range(i+1,length):
            if nums[j]<first:
                second=nums[j]
                result.append((first,second))
    print(result)
    return result

class Solution2:
    def InverPairs(self,data):
        if len(data)==0:
            return 0
        copy_num=data[:]
        cnt=self.InverCore(data,copy_num,0,len(data)-1)
        return cnt%1000000000000000000007
    def InverCore(self,data,copy,statr,end):
        if statr==end:
            copy[statr]=data[statr]
            return 0
        mid=(statr+end)//2
        # 分两半来排序
        left=self.InverCore(copy,data,statr,mid)
        right=self.InverCore(copy,data,mid+1,end)
        i,j=statr,mid+1
        index, cnt= statr,0
        while j<=mid and j<=end:
            if data[i]<=data[j]:
                #把较大数字从后往前复制到辅助数组，确保辅助数组是递增排序的
                copy[index]=data[i]
                i+=1
            else:
                copy[index]=data[j]
                cnt+=mid-i+1
                j+=1
            index+=1
        while i<=mid:
            copy[index]=data[i]
            i+=1
            index+=1
        while j<end:
            copy[index]=data[j]
            j+=1
            index+=1
        return left+right+cnt
