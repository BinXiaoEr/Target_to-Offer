def find(matrix, rows, columns, target):
    row, column = 0, columns - 1
    while row < rows and column >= 0:
        if target < matrix[row][column]:
            column -= 1
        elif target > matrix[row][column]:
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
print(find(test,4,4,0))
