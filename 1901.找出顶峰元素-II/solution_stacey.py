def findPeakGrid(mat):
    row, col = len(mat), len(mat[0])

    def find_max(i, j):
        cur_i, cur_j = i, j
        for r, c in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            if 0 <= r < row and 0 <= c < col and mat[r][c] > mat[cur_i][cur_j]:
                cur_i, cur_j = r, c
        return cur_i, cur_j

    i, j = 0, 0
    cur = mat[i][j]
    while 0 <= i < row and 0 <= j < col:
        if (i + 1 >= row or cur > mat[i + 1][j]) and (j + 1 >= col or cur > mat[i][j + 1]) and (
                j - 1 < 0 or cur > mat[i][j - 1]) and (i - 1 < 0 or cur > mat[i - 1][j]):
            return [i, j]
        i, j = find_max(i, j)
        cur = mat[i][j]
    return i, j

inp = [[1,2,6],[3,4,5]]
findPeakGrid(inp)