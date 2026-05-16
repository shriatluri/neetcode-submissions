from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        fromPacific: Set[Tuple[int, int]] = set()
        fromAtlantic: Set[Tuple[int, int]] = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Build starting positions for Pacific
        for c in range(cols):
            fromPacific.add((0, c))          # top row
            fromAtlantic.add((rows - 1, c))  # bottom row
        
        for r in range(rows):
            fromPacific.add((r, 0))          # left column
            fromAtlantic.add((r, cols - 1))  # right column
        
        def dfs_iterative(starts: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited: Set[Tuple[int, int]] = set()
            stack = []
            
            # Initialize stack and visited with all starting cells
            for cell in starts:
                stack.append(cell)
                visited.add(cell)
            
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Bounds check
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    # Already visited
                    if (nr, nc) in visited:
                        continue
                    # Height condition: neighbor must be >= current
                    if heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            
            return visited
        
        pacificVisited = dfs_iterative(fromPacific)
        atlanticVisited = dfs_iterative(fromAtlantic)
        
        # Overlap between pacificVisited and atlanticVisited
        result = [[r, c] for (r, c) in pacificVisited & atlanticVisited]
        return result
