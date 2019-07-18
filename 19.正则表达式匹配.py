def match(s,pattern):
    if len(s) == 0 and len(pattern) == 0:
        return True
    if len(s) > 0 and len(pattern) == 0:
        return False
    #如果第二个字符是*
    if len(pattern)>1 and pattern[1]=='*':
        if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='*'): \
            # 如果第一个字符匹配，2种可能
            # 1、模式后移2位，认为‘ * ’前的字符在s中只出现一次。；
            # 2、字符串移1位,认为‘ * ’前的字符在s中出现不止一次
            return match(s,pattern[2:]) or match(s[1:], pattern)
        else:
            # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
            return match(s, pattern[2:])
    #如果第二个字符不是*
    if len(s)>0 and(s[0]==pattern[0] or pattern[0]=='.'):
        return match(s[1:],pattern[1:])
    else:
        return False
print(match('aaa','ab*a'))
