class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # get depth and width of mine
        ans = 0 # value to return

        def dfs(x, y, gold):
            gold += grid[x][y]  # accumulate
            nonlocal ans    # delcare non local var
            ans = max(ans, gold)    # overwrite ans if more gold mined

            temp = grid[x][y]   # temporarily store cell value
            grid[x][y] = 0  # set mined cell as 0 to avoid mining over once

            # left, right, up, down
            nextstep = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
            for new_x, new_y in nextstep:
                # avoid out of range in depth or width and minming a 0 cell
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] > 0:
                    dfs(new_x, new_y, gold) # mine next cell

            grid[x][y] = temp # retore gold in mined grid cell

        # iterate all cell in grid except 0 gold cells, excecute as first cell to mine
        for i in range(m):
            for k in range(n):
                if grid[i][k] != 0:
                    dfs(i, k, 0)

        return ans  # max gold mined using best route