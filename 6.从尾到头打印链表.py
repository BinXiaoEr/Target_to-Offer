from 链表 import Linklist

#定义节点类型
class Node(object):
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

def PrintListReverse(head):
    stack=[]
    node=head
    while node is not None:
        stack.append(node.elem)
        node=node.next
    print(stack[::-1])
def PintListReverse_DiGui(node):
    if node is not None:
        if node.next is not None:
            PintListReverse_DiGui(node.next)
        print(node.elem,end=' ')


if __name__ == '__main__':
    linklist = Linklist()
    for i in range(5):
        linklist.append(i)
    linklist.travel()
    linklist.insert(3, 7)
    print("#" * 30)
    PintListReverse_DiGui(linklist.head)
    print("")
    print("+" * 30)
    PrintListReverse(linklist.head)
    print("*"*30)
    linklist.travel()
    print(linklist.search(4))
    linklist.remove(7)
    linklist.travel()
