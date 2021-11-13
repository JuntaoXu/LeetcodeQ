class Solution:
    def numIslands(self, grid):
        col = len(grid[0])
        row = len(grid)
        def search(i,j):
            if not 0<= i < row or not 0 <= j < col or grid[i][j]=='0': return
            grid[i][j] = '0'
            search(i-1, j)
            search(i+1, j)
            search(i, j-1)
            search(i, j+1)
        num = 0
        for i in row:
            for j in col:
                if grid[i][j] == '1':
                    search(i,j)
                    num +=1
        return num