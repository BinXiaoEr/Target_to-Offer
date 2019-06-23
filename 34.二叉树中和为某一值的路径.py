
class Node(object):
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None

#定义树
class Tree():
    def __init__(self):
        self.root=None
    #添加树
    def add(self,item):
        node=Node(item)
        if self.root==None:
            #如果根节点为空
            self.root=node
        else:
            queue=[]
            queue.append(self.root)
            while queue:
                cur_node=queue.pop(0)
                #取出列表第一个元素额
                if cur_node.left is None:
                    cur_node.left=node
                    return
                else:
                    #如果当前节点的左子树不为空将其添加至列表中
                    queue.append(cur_node.left)
                if cur_node.right is None:
                    cur_node.right =node
                    return
                else:
                    queue.append(cur_node.right)

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def get_path(self,root,expectNumber,path_list,result):
        new_val=expectNumber-root.val
        path_list.append(root.val)
        if new_val==0 and root.left is None and root.right is None:
            print(path_list)
            result.append(path_list[:])
        if root.left is not None:
            self.get_path(root.left,new_val,path_list,result)
        if root.right is not None:
            self.get_path(root.right,new_val,path_list,result)
        path_list.pop()
    def FindPath(self, root, expectNumber):
        # write code here
        if root.val>expectNumber or root is None:
            return
        path_list=[]
        result=[]
        self.get_path(root,expectNumber,path_list,result)
        return result

if __name__=='__main__':
    tree = Tree()
    for i in range(7):
        tree.add(i)
    a=Solution()
    print(a.FindPath(tree.root,4))