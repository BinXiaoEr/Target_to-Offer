# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        lengtha=0
        lengthb=0
        if pHead1 is None or pHead2 is None:
            return
        p1=pHead1
        p2=pHead2
        while p1:
            lengtha+=1
            p1=p1.next
        while p2:
            lengthb+=1
            p2=p2.next
        length=lengtha-lengthb
        #把p1都当作长链表处理
        if lengtha<lengthb:
            pHead1,pHead2=pHead2,pHead1
            length=lengthb-lengtha
        for i in range(length):
            pHead1=pHead1.next
        while pHead1 is not None and pHead2 is not None :
            if pHead1==pHead2:
                return pHead1
            pHead1=pHead1.next
            pHead2=pHead2.next
        return 
