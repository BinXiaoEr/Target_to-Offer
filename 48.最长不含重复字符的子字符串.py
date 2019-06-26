def lengthOfLongestSubstring(s):
    if len(s)==0:
        return 0
    culen=0#当前长度
    maxlen=0#所有的最大长度
    pos=[-1]*26
    for i in range(len(s)):
        index=pos[ord(s[i])-97]
        #h获取当前字符对应的在pos中的位置（a-z 对应0-26） 用ascii码计算
        #如果没有出现过 或者出现过 但是最近出现的距离大于culen 即不在这个长度的范围内
        if index<0 or i-index>culen:
            culen+=1
        else:
            #出现过 并且就在这个目前的字符串里
            if culen>maxlen:
                maxlen=culen
            #最新的距离 是当前位置-当前字符上一次最近出现的距离
            culen=i-index

        #记录对应字符的最近出现的位置
        pos[ord(s[i])-97]=i
    if culen>maxlen:
        maxlen=culen

    return maxlen
print(lengthOfLongestSubstring('aracbcacfr'))