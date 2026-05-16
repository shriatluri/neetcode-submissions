class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Contraints:
        - 1 <= n <= 100
        - 0 <= edges.length <= n * (n - 1) / 2
        Valid tree - Connected and Acyclic

        We need to perform a dfs and make sure
        - Need to make sure that the first val of the node exists
        - As we traverse, the second val of the node has not been in the visited set (Acyclic)
        If both these conditions are true, then we return True, else false
        '''

        # automatic cycle
        if len(edges) > (n - 1):
            return False
        
        # create an adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # we use this to check if we are back at a node
        visited = set()

        # pass in parent to make sure we don't have false loops
        def dfs(node, parent):
            # if cycle
            if node in visited:
                return False
            visited.add(node)
            # look at all neighbors
            for nei in adj[node]:
                # parents alr been visited
                if nei == parent:
                    continue
                # if we found a cycle
                if not dfs(nei, node):
                    return False
            return True
        
        # connected and no cycles
        return dfs(0, -1) and len(visited) == n
                



        

        

