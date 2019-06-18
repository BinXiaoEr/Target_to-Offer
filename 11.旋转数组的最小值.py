def min_nums(numbers):
    length=len(numbers)
    first=0
    last=length-1
    mid=first#如果把第一个数组进行反转则最后一个数字就是最小的，所以要把mid设为first
    while(numbers[first]>=numbers[last]):
        if(last-first==1):
            mid=last
            break
        mid=(first+last)//2
        if(numbers[first]==numbers[last] and numbers[first]==numbers[mid]):
            return MinInorder(numbers,first,last)
        if(numbers[first]<numbers[mid]):
            first=mid
        elif numbers[mid]<numbers[last]:
            last=mid
    return numbers[mid]

def MinInorder(numbers,first,last):
    result=numbers[first]
    for i in range(first+1,last+1):
        if result>numbers[i]:
            result=numbers[i]
    return result
print(min_nums([3,4,5,6,7,1,2]))

print(min_nums([1,1,1,0,1,1]))