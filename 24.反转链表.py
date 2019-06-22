class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        new_head = None
        next_node = None
        node = pHead
        while node is not None:
            #保存当前节点的下一节点
            next_node = node.next
            #将该节点的下一节点指向新的链接的表头
            node.next = new_head
            #将次表头更换为新的节点
            new_head = node
            #重置节点
            node = next_node
        return new_head


