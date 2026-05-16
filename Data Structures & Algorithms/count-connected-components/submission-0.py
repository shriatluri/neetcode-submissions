class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create the adj list
        count = 0
        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    dfs(neigh)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count

