
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        head=root
        if not head:
            return
        queue = []
        queue.append(head)
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                print(node.elem,end='')
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)

if __name__=='__main__':
    tree = Tree()
    for i in range(7):
        tree.add(i)
    tree.add(4)
    tree.add(3)
    a=Solution()
    a.PrintFromTopToBottom(tree.root)