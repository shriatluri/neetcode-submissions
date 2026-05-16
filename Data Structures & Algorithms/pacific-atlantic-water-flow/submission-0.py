'''
Water flows downhill (to equal or lower height).
Instead of checking from every cell → both oceans (inefficient), reverse the flow.
Start DFS/BFS from the ocean edges:
    Pacific: top row + left col
    Atlantic: bottom row + right col
From each starting cell, only move to neighbors with height ≥ current (reverse direction of flow).
Record visited cells for each ocean in two sets.
Final result = cells in atl and pac set
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # viisted cells from each ocean
        atl, pac = set(), set()

        def dfs(r, c, visited):
            # check if alr visited
            if (r, c) in visited:
                return
            visited.add((r,c))

            # logic - visit up, right, down, left
            for ar, ac in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                tr, tc = r + ar, c + ac
                # in bounds and since we are going to the middle, we reverse
                if 0 <= tr < ROWS and 0 <= tc < COLS and heights[tr][tc] >= heights[r][c]:
                    dfs(tr, tc, visited)
        # borders
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        
        res = []
        # return ones that meet pac and atl
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        
