# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return (left if left>right else right)+1
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return abs(self.judege_length(pRoot.left)-self.judege_length(pRoot.right))<2 and self.IsBalanced_Solution(pRoot.left)and self.IsBalanced_Solution(pRoot.right)

    def judege_length(self, root):
        if root is None:
            return 0
        left = self.judege_length(root.left)
        right = self.judege_length(root.right)
        return (left if left > right else right) + 1

