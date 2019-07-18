#定义树的节点
class Node(object):
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None

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
                if cur_node.lchild is None:
                    cur_node.lchild=node
                    return
                else:
                    #如果当前节点的左子树不为空将其添加至列表中
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild =node
                    return
                else:
                    queue.append(cur_node.rchild)

    #广度遍历非递归
    def breadth_travel(self):
        if self.root==None:
            return
        queue=[]
        queue.append(self.root)
        while queue:
            node=queue.pop(0)
            print(node.elem,end=' ')
            if node.lchild!=None:
                queue.append(node.lchild)
            if node.rchild!=None:
                queue.append(node.rchild)
        print('')

    def breadth_travel_two(self):
        if self.root==None:
            return
        queue=[]
        queue.append(self.root)
        while queue:
            length=len(queue)
            for i in range(length):
                node=queue.pop(0)
                print(node.elem,end=' ')
                if node.lchild != None:
                    queue.append(node.lchild)
                if node.rchild != None:
                    queue.append(node.rchild)
        print('')

    #深度遍历 非递归 前序遍历 根 左 右
    def deep_travel_qianxu(self):
        if self.root==None:
            return
        queue=[]
        queue.append(self.root)
        while queue:
            cur=queue.pop()
            print(cur.elem,end=' ')
            #前序遍历 根 左 右
            #先放入右节点再放入作节点
            if cur.rchild is not None:
                queue.append(cur.rchild)
            if cur.lchild is not None:
                queue.append(cur.lchild)
        print('')
    #左根右
    """
    1. 使用一个栈保存结点（列表实现）；
    2. 如果结点存在，入栈，然后将当前指针指向左子树，直到为空；
    3. 当前结点不存在，则出栈栈顶元素，并把当前指针指向栈顶元素的右子树；
    4. 栈不为空，循环2、3。
    """
    def deep_travel_zhongxu(self):

        if not self.root:
            return
        stack = []
        cur=self.root
        while cur or stack:
            #将当前节点的左节点都入栈
            while cur:
                stack.append(cur)
                cur = cur.lchild
            # 获取当前最左节点
            if stack:
                a = stack.pop()
                cur = a.rchild
                print(a.elem,end=' ')
        print('')
    #左 右 根
    def deep_travel_houxu(self):
        cur=self.root
        stack = [cur]
        stack2 = []
        while len(stack) > 0:
            cur = stack.pop()
            stack2.append(cur)
            if cur.lchild:
                stack.append(cur.lchild)
            if cur.rchild:
                stack.append(cur.rchild)
        while len(stack2) > 0:
            node = stack2.pop()
            print(node.elem,end=' ')

        print('')

    #深度遍历递归
    def preorder(self, node):
        # 先序遍历 根 左 右
        if node == None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        # 中序遍历 左 根 右
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def proorder(self, node):
        # 后序遍历 左 右 根
        if node == None:
            return
        self.inorder(node.lchild)
        self.inorder(node.rchild)
        print(node.elem, end=" ")

if __name__=='__main__':
    tree=Tree()
    for i in range(7):
        tree.add(i)
    tree.breadth_travel_two()
    print("*"*20)
    tree.deep_travel_qianxu()
    print("*" * 20)
    tree.deep_travel_zhongxu()
    print("*"*20)
    tree.deep_travel_houxu()