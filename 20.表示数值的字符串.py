def isNumeric(s):
    isAllowDot = True  # 表示还没出现小数点.
    isAllowE = True    # 表示还没出现e/E   e/E/. 都是只能出现一次的..
    for i in range(len(s)):
        if i == 0 and s[i] == 'e': # e前面必须有数值
            return False
        if s[i] in "+-" and (i == 0 or s[i-1] in "eE") and i < len(s)-1: # 把i=0的情况单拎出来,因为后面涉及i-1的判断
            continue
        elif isAllowDot and s[i] == ".": # 有小数点,则其前面的A可以是0,但后面的B必须右值
            isAllowDot = False
            if i < len(s)-1 and s[i+1] not in "0123456789": # 此处修改，"100."也是数字
                return False
        elif isAllowE and s[i] in "Ee":
            isAllowDot = False # 这个有必要! 使得e后面的小数点.会return False
            isAllowE = False  # 这里是需要的,因为e的指数不可为小数.
            if (i >= len(s)-1) or (s[i+1] not in "0123456789+-") or s[i-1] not in "0123456789":
                return False
        elif s[i] not in "0123456789":  # 排除第一个字符是e的情况.
            return False
    return True