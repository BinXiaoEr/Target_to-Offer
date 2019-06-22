class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.jude(pRoot,pRoot)
    def jude(self,q,p):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.jude(p.left, q.right) and self.jude(p.right, q.left)
        return False