class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.max_count = 0

        def dfs(r, c) -> int:
            # first check if in bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            # set to water
            grid[r][c] = 0
            count = 1
            # check all directions
            for nr, nc in ((0,1), (0,-1), (1,0), (-1,0)):
                count += dfs(r + nr, c + nc)
            return count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.max_count = max(self.max_count, dfs(r,c))
        return self.max_count