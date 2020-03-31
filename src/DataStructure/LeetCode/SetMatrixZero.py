def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0

    for num in range(R):
        for c in range(C):
            print(matrix[num][c])
            print(",")
        print("\n")


input =[
  [0,1]
]

setZeroes(input)