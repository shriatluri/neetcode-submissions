from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    self.bfs(grid, r, c, visited)
        
        return count
    
    def bfs(self, grid, r, c, visited):
        bfsQueue = deque()
        visited.add((r,c))
        bfsQueue.append((r,c))

        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        while bfsQueue:
            cr, cc = bfsQueue.popleft()

            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if (grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        bfsQueue.append((nr, nc))

