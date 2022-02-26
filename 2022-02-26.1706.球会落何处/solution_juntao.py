def dfs(x, y, m, n, grid):
    if x >= m:
        return y
    if grid[x][y] == -1:
        if y - 1 < 0 or grid[x][y - 1] == 1:
            return -1
        else:
            return dfs(x + 1, y - 1, m, n, grid)
    else:
        if y + 1 >= n or grid[x][y + 1] == -1:
            return -1
        else:
            return dfs(x + 1, y + 1, m, n, grid)


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        answer = []
        for i in range(n):
            answer.append(dfs(0, i, m, n, grid))
        return answer