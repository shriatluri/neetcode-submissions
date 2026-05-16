from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        edgeList = defaultdict(list)
        result = 0

        for a,b in edges:
            edgeList[a].append(b)
            edgeList[b].append(a)


        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in edgeList[node]:
                dfs(neighbor)

        for i in range(0, n):
            if i not in visited:
                dfs(i)
                result += 1
        
        return result

        
        