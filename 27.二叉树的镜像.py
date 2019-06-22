
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        root.left, root.right = root.right, root.left

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)