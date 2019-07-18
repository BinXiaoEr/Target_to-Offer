from 链表 import Linklist

#定义节点类型
class Node(object):
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    def printListFromTailToHead(self, listNode):
        stack = []
        node = listNode
        while node is not None:
            stack.append(node.val)
            node = node.next
        return stack[::-1]


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
