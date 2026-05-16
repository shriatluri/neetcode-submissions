from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        result = 0
        directions = [(0,-1), (0,1), (-1,0), (1,0)]

        def dfs(i, j):
            if (
                i < 0 or j < 0 or
                i >= len(grid) or j >= len(grid[0]) or
                grid[i][j] == "0" or
                (i, j) in visited
            ):
                return
            
            visited.add((i,j))
            
            for x, y in directions:
                dfs(i + x, j + y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if tuple((i,j)) in visited:
                    continue

                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        
        return result
                
                



