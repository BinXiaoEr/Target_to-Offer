class Solution:
    def IsPopOrder(self, pushV, popV):
        push,pop =pushV,popV
        if not push or not pop or (len(push) != len(pop)):
            return False
        new_list = []
        flag = False
        while push or new_list:
            while (len(new_list) == 0 or new_list[-1] != pop[0]):
                # 判断push是否还有元素
                if len(push) == 0:
                    break
                # 如果辅助栈为空或者辅助栈的栈顶不是要出序列的第一个
                num = push.pop(0)
                new_list.append(num)
            # 判断当前辅助栈栈顶是否和pop栈第一个相同 如果还不相同且上方已经可能push没有元素了  所以就不能存在
            if new_list[-1] != pop[0]:
                break
            new_list.pop(-1)
            pop.pop(0)
        if not new_list and not pop and not push:
            flag = True
        return flag
