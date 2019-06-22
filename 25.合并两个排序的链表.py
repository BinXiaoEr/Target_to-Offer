# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        #如果某个链表为空 则将另一个链表返回
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        new_head = None
        if pHead1.val < pHead2.val:
            new_head = pHead1
            new_head.next = self.Merge(pHead1.next, pHead2)
        else:
            new_head = pHead2
            new_head.next = self.Merge(pHead1, pHead2.next)
        return new_head

class Solution:
    def Merge( self,l1, l2):
        p_node= ListNode(0)
        pre =p_node
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                p_node.next =l1
                l1 =l1.next
            else:
                p_node.next = l2
                l2 = l2.next
            #将该节点往后移动
            p_node = p_node.next
        if l1 is not None:
            p_node.next = l1
        else:
            p_node.next = l2

        return pre.next#ｐｒｅ指向ｎｏｄｅ（０）　所以其下一个是新的节点
