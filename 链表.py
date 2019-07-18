#定义节点类型
class Node(object):
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

#定义单链表
class Linklist(object):
    def __init__(self,none=None):
        self.head=none
    #判断链表是否为空
    def is_empty(self):
        return self.head==None
    #获取链表长度
    def length(self):
        cur=self.head#获取首元节点
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    #遍历链表
    def travel(self):
        cur=self.head
        while cur!=None:
            print(cur.elem,end=" ")
            cur =cur.next
        #输出一个换行
        print('')
    #首部加元素
    def add(self,item):
        #将数据转换为节点类型
        node=Node(item)
        #新的节点指向首元节点
        node.next=self.head
        #新的节点变成首元节点
        self.head=node
    #尾部加元素
    def append(self,item):
        node=Node(item)
        #判断是否为空
        if self.is_empty():
            #为空此节点就是首元节点
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                # 遍历到最后一个节点
                cur=cur.next
            cur.next=node
    #在指定位置添加节点
    def insert(self,pos,item):
        if pos<0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            node=Node(item)
            cur=self.head
            count=0
            while count<(pos-1):
                count+=1
                cur= cur.next
            node.next=cur.next
            cur.next=node
    #删除指定值的节点
    def remove(self,item):
        cur=self.head
        pre=None
        while cur != None:
            if cur.elem==item:
                #如果当前节点的值符合要求
                if cur==self.head:
                    #如果符合的节点是首元节点
                    self.head=cur.next
                    break
                else:
                    #从当前节点的前一个节点直接指向当前节点的下一个节点
                    pre.next=cur.next
                    break
            else:
                #当前节点不符合
                pre=cur#记录当前节点的位置
                cur=cur.next
        #查询某个值是否存在
    def search(self,item):
        cur=self.head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False

if __name__=='__main__':
    linklist=Linklist()
    for i in range(5):
        linklist.append(i)
    linklist.travel()
    linklist.insert(3,7)
    linklist.travel()
    print(linklist.search(4))
    linklist.remove(7)
    linklist.travel()