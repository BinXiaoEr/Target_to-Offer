# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s=s.split(' ')
        begin=0
        end=len(s)-1
        while begin<end:
            s[begin],s[end]=s[end],s[begin]
            begin+=1
            end-=1
        print(' '.join(s))
        return ' '.join(s)




# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s is None:
            return ""
        length=len(s)
        if length>0 and n>0 and n<length:

            left=self.ReverseSentence(list(s[:n]))
            right=self.ReverseSentence(list(s[n:]))
            number=left+right
            return self.ReverseSentence(list(number))
        return s
    def ReverseSentence(self, s):
        # write code here
        begin=0
        end=len(s)-1
        while begin<end:
            s[begin],s[end]=s[end],s[begin]
            begin+=1
            end-=1
        return ''.join(s)
