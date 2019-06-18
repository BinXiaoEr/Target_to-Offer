class Node(object):
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None
        self.parent=None

def GetNext(node):
    if node is None:
        return None
    if node.rchilid:
        node=node.rchild
        while node.lchild:
            node=node.lchild
        return node
    else:
        while node.parent:
            if node==node.parent.lchild:
                return node.parent
            node=node.parent
    return None
