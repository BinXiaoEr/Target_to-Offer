# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.result=[]
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None or k==0:
            return None
        self.GetNode(pRoot)
        if len(self.result)<k:
            return None
        return self.result[k-1]
    def GetNode(self,pRoot):
        if pRoot.left:
            self.GetNode(pRoot.left)
        self.result.append(pRoot)
        if pRoot.right:
            self.GetNode(pRoot.right)
