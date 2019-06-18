class Node(object):
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None

def BuildTree(pre,mid):
    # if (len(pre)or len(mid))==0:
    #     return None
    lon=len(pre)
    if lon==0:
        return None
    elif lon==1:
        return Node(pre[0])
    else:
        mid_index=mid.index(pre[0])#获取节点在中序中的位置 切割左右两边
        node=Node(pre[0])
        node.lchild=BuildTree(pre[1:mid_index+1],mid[:mid_index])
        node.rchild=BuildTree(pre[mid_index+1:],mid[mid_index+1:])
        return node

if __name__=='__main__':
    pre = [1, 2, 4, 5, 3, 6, 7]
    mid = [4, 2, 5, 1, 6, 3, 7]
    tree=BuildTree(pre,mid)
