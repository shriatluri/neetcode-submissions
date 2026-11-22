from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[0,1], [0, -1], [-1, 0], [1, 0]]
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "1":
                    continue
                
                islands += 1
                grid[r][c] = "0"
                stack = [[r,c]]

                while stack:
                    currR, currC = stack.pop()

                    for dirR, dirC in directions:
                        newR = currR + dirR
                        newC = currC + dirC

                        if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == "1":
                            stack.append([newR, newC])
                            grid[newR][newC] = "0"
        
        return islands
                
            





