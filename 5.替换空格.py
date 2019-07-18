
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_strs = []
        for i in range(len(s)):
            if s[i] == ' ':
                # strs[i]='%20'
                new_strs.append('%20')
            else:
                new_strs.append(s[i])
        return ''.join(new_strs)

