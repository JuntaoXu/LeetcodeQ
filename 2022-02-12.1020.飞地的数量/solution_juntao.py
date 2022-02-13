class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        def makeSea(i, j):  # turn land to sea if on edge
            grid[i][j] = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # check adjacent cell
                if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                    makeSea(i + di, j + dj)  # recursion, turn adjacent land to sea

        for j in range(n):  # interate edges
            if grid[0][j] == 1:
                makeSea(0, j)
            if grid[m - 1][j] == 1:
                makeSea(m - 1, j)
        for i in range(1, m - 1):  # avoid excess check
            if grid[i][0] == 1:
                makeSea(i, 0)
            if grid[i][n - 1] == 1:
                makeSea(i, n - 1)

        return sum(row.count(1) for row in grid)  # return count number of land left
