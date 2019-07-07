def MaxDiff(numbers):
    if len(numbers)<2:
        return 0
    min_num=numbers[0]
    maxdiff=numbers[1]-min_num
    for i in range(len(numbers)):
        if numbers[i-1]<min_num:
            min_num=numbers[i]
        cur=numbers[i]-min_num
        maxdiff=cur if maxdiff<cur else maxdiff

    print(maxdiff)
MaxDiff([9,11,8,5,7,12,16,14])