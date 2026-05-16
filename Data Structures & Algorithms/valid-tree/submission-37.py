from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeList = defaultdict(list)
        visited = []

        if edges == []:
            return True

        if n == 1:
            return False

        for a, b in edges:
            edgeList[a].append(b)
            edgeList[b].append(a)
        
        def dfs(node, parent):
            visited.append(node)
            
            for nei in edgeList[node]:
                if nei == parent:
                    continue

                if nei in visited:
                    return False

                dfs(nei, node)
            
            return True

        if not dfs(0, 0):
            return False

        if len(visited) != n:
            return False

        return True
 
