
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        nums=numbers
        counts = {}
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
        list1 = sorted(counts.items(), key=lambda x: x[1])
        if list1[-1][-1] > len(nums) // 2:
            return (list1[-1][0])
        else:
            return 0

    def MoreThanHalfNum_Solution2(self, numbers):
        if len(numbers)<=0:
            return 0
        reslut=numbers[0]
        count=1
        for i in range(1,len(numbers)):
            if count==0:
                reslut=numbers[i]
                count=1
            elif numbers[i]==reslut:
                count+=1
            else:
                count-=1
        if self.CheckMore(numbers,reslut):
            return reslut
        return 0
    #检验当前次数多的数字次数是不是超过一般
    def CheckMore(self,number,result):
        count=0
        for i in range(len(number)):
            if number[i]==result:
                count+=1
        if count*2<=len(number):
            return False
        return True

a=Solution()
print(a.MoreThanHalfNum_Solution2([1,1,2,2,3]))

#数据库索引、存储过程有什么作用
#优缺点分别是什么