

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array==[[]]:
            return False
        rows=len(array)#行
        row=0
        columns=len(array[1])#列
        column=columns-1
        while row < rows and column >= 0:
            if target < array[row][column]:
                column -= 1
            elif target > array[row][column]:
                row += 1
            else:
                return True
        return False


test = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]
a=Solution()
print(a.Find(4,[[]]))
