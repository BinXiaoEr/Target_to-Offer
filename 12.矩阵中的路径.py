def hasPath(matrix, rows, cols, path):
    flagmartix = [True] * rows * cols
    # 设置遍历到的节点标志
    for i in range(rows):
        for j in range(cols):
            if   hasPathPoint(matrix, rows, cols, i, j, path, flagmartix):
                return True

    return False


def hasPathPoint(martix, rows, cols, i, j, path, flagmartix):
    if not path:
        return True
    index = i * cols + j  # 获取当前访问节点的位置
    if i < 0 or i >= rows or j < 0 or j >= cols or martix[index] != path[0] or flagmartix[index] == False:
        return False
    # 不满足上方条件 说明此时这个节点是对应路径中的节点
    flagmartix[index] = False
    if (hasPathPoint(martix, rows, cols, i + 1, j, path[1:], flagmartix) or
            hasPathPoint(martix, rows, cols, i - 1, j, path[1:], flagmartix) or
            hasPathPoint(martix, rows, cols, i, j - 1, path[1:], flagmartix) or
            hasPathPoint(martix, rows, cols, i, j + 1, path[1:], flagmartix)
    ):
        return True
    # 如果当前节点的上下左右无法走下去，仍要把当前位置标志设为True 表示没有访问过
    flagmartix[index] = True
    return False

if __name__=='__main__':
    martix=['A','B','C','E','S','F','C','S','A','D','E','F']
    path=['A','B','C','C','E','D']
    print(hasPath(martix,3,4,path))