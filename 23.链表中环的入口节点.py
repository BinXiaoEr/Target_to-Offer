def GetNode(head):
    node =JudgeCircle(head)#
    if node is None:
        return None
    #如果判断的环方法返回的是None说明没有环
    count=1
    node1=node
    # count为环中节点的数目 获取环中节点的数目
    while node1.next is not node:
        node1=node1.next
        count+=1

    node1=head
    for i in range(count):
        node1=node1.next
    #先移动nodel1 次数为环中节点的数目

    #再移动node1和node2
    node2=head
    while node1 !=node2:
        node1=node1.next
        node2=node2.next
    return node2
#判断有无环
def JudgeCircle(head):
    first=head.next
    last=first.next
    while first is not None and last is not None:
        if first==last:
            #返回环中的一个节点
            return last
        first=first.next#慢指针走一步
        last=last.next#快指针走两步
        if last is not None:
            last=last.next
        # 快指针走两步
    return None
