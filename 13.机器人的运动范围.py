def move_count(rows, cols, k):
    if k < 0 or rows <= 0 or cols <= 0:
        return 0
    moved = [True] * rows * cols
    # 设置判断每个坐标被访问的标志
    count = moving_count(rows,cols,k,0,0,moved)
    return count

#向上下左右进行访问
def moving_count(rows, cols, k, row, col, moved):
    count = 0
    if checked(rows, cols, k, row, col, moved):
        moved[row * cols + col] = False
        count=1+moving_count(rows, cols, k, row-1, col, moved)+moving_count(rows, cols, k, row, col-1, moved)+moving_count(rows, cols, k, row+1, col, moved)+moving_count(rows, cols, k, row, col+1, moved)
    return count

#判断 每次坐标是否符合要求，符合要求则可以继续访问
def checked(rows, cols, k, row, col, moved):
    if (row>= 0 and col >= 0 and row < rows and col < cols
            and (nums(row) + nums(col) <= k )
            and moved[row * cols + col] == True):
        return True
    return False

#坐标转换为数位之和
def nums(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

if __name__ =='__main__':
    print(move_count(4,4,2))