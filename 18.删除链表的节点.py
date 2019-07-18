#定义节点类型
class Node(object):
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_
def DeleteNode(head,target):
    #target不是尾节点
    if(target.next is not None):
        node=target.next
        target.next=node.next
        target.elem=node.elem

        #将目标的下一节点删除了 target替换了下一节点
        node.next=None
        node.elem=None

    elif head==target:
        #target是首元节点
        target.next=None
        target.elem=None
    else:
        #删除的节点在尾部 则仍然要通过O(n)删除
        node=head
        while node !=target:
            node=node.next
        node.next=None
        target.next=None
        target.elem=None


