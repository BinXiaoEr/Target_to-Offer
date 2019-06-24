# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.head=None
        self.tail=None
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return
        cur = pRootOfTree
        if cur.left:
            self.Convert(cur.left)
        # 将左子节点换成前序 右子节点换成后序
        if self.head is None:
            self.head=pRootOfTree
            self.tail=pRootOfTree
        else:
            pRootOfTree.left = self.tail
            self.tail.right=pRootOfTree
            self.tail=pRootOfTree
        if cur.right:
            self.Convert(cur.right)
        return self.head

