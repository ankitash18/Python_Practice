def searchMatrix(self, matrix, target):
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        return False

    n = len(matrix)
    m = len(matrix[0])
    i = 0
    j = m - 1

    while (i < n and j >= 0):
        num = matrix[i][j]

        if num == target:
            return True
        elif num > target:
            j -= 1
        else:
            i += 1
    return False