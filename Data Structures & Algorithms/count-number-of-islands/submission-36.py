from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "1":
                    continue

                islands += 1
                stack = [[r, c]]

                while stack:
                    curR, curC = stack.pop()
                    for direction in dirs:
                        nr, nc = [curR + direction[0], curC + direction[1]]

                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                            stack.append([nr, nc])
                            grid[nr][nc] = "0"
        
        return islands


            





