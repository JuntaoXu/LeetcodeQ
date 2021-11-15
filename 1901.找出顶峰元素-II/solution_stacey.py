def findPeakGrid(mat):
    row, col = len(mat), len(mat[0])
    i, j = 0, 0
    cur = mat[i][j]
    while 0 <= i < row and 0 <= j < col:
        print(i,j)
        if (i + 1 >= row or cur > mat[i + 1][j]) and (j + 1 >= col or cur > mat[i][j + 1]):
            return [i, j]
        if i + 1 < row and (j + 1 >= col or mat[i + 1][j] >= mat[i][j + 1]):
            i += 1
        elif j + 1 < col and (i + 1 >= row or mat[i][j + 1] >= mat[i + 1][j]):
            j += 1
        cur = mat[i][j]

inp = [[1,2,6],[3,4,5]]
findPeakGrid(inp)