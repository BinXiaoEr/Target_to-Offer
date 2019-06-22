# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        self.stack.append(node)
        #如果min_stack为空 或者当前结点值小于等于栈最后的那个值
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
    def pop(self):
        #如果当前栈顶元素和辅助栈定元素相同则 也要移除辅助栈顶元素
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.min_stack[-1]

a=Solution()
a.push(6)
a.push(4)
a.push(3)
print(a.min())
a.pop()
a.pop()
print(a.min())