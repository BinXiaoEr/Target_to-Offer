class QueueWithTwoStack(object):
    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]
    def appendTail(self,x):
        #数据统一插入stack1
        self.__stack1.append(x)

    def deleteHead(self):
        #判断stack2有无数据
        #r若有则stack2的栈顶元素就是队列的队头
        #若没有则把stack1数据移到stack2
        #123->321 队列的首部 变成栈顶 则可以弹出了
        if self.__stack2:
            #如果stack2不为空则栈顶的元素就是stack队列首元素
            self.__stack2.pop()
        else:
            if self.__stack1:
                while self.__stack1:
                    self.__stack2.append(self.__stack1.pop())
                return self.__stack2.pop()
            else:
                return None