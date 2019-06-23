# encoding:utf8
class RandomListNode():
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self,pHead):
        if pHead == None:
            return None
        # 复制节点在原节点之后
        pCur = pHead
        while (pCur != None):
            node = RandomListNode(pCur.label)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next

        # 复制random节点
        pCur = pHead
        while (pCur != None):
            if pCur.random != None:
                pCur.next.random = pCur.random.next
               # pCur.next.random=pCur
            pCur = pCur.next.next

        # 将新旧链表分离
        head = pHead.next#新的表 奇数是新表 偶数是旧表
        cur = head
        pCur = pHead#旧的表
        while(pCur!=None):
            pCur.next=pCur.next.next
            if cur.next is not None:
                #如果奇数的下一个还存在 则说明偶数还有一个复制的奇数
                cur.next=cur.next.next
            cur=cur.next
            pCur=pCur.next
        return head


