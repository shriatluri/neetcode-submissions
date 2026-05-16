class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            # make sure that we are at a valid position
            # in bounds and equal to 0
            if i < 0 or r <= i or j < 0 or c <= j or grid[i][j] != '1':
                return
            else:
                # mark all the neighbors as 0 if they are 1
                grid[i][j] = '0'
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    islands += 1
                    # this will make sure that we can mark 
                    dfs(i, j)
        return islands