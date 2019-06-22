# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def RertunNum(head,k):
    if head is None:
        return None
    pre=post=head
    for i in range(k):
        if pre==None:
            #如果k超出链表长度直接返回None
            return None
        pre=pre.next
        #快慢指针同时往前走 当快指针走到头 就是慢指针走到倒数第k个位置

        while pre!=None:
            pre=pre.next
            post=post.next
        return post