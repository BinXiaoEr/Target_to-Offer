# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        n1=num1
        n2=num2
        carry = 1
        while carry:
            s = n1 ^ n2
            carry = 0xFFFFFFFF & ((n1 & n2) << 1)
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            n1 = s
            n2 = carry
        return n1