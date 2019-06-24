# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        if root is None:
            return '$'
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)
        # write code here
    def Deserialize(self, s):
        # write code here
        print(type(s))
        s=s.split(',')
        return self.Get_Tree(s)
    def Get_Tree(self,s):
        if len(s)<=0:
            return None
        val=s.pop(0)
        root=None
        if val!='$':
            root=TreeNode(int(val))
            root.left=self.Get_Tree(s)
            root.right=self.Get_Tree(s)
        return root
if __name__=='__main__':
    s='1,2,4,$,$,$,3,5,$,$,6,$,$'
    a=Solution()
    print(a.Deserialize(s))