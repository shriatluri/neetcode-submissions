"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
Connected undirected graph, bfs would be the best method here
the index (1-indexed) is the val we are at

Strategy: Clone each one of the nodes
1. Cloned dict to clone each of the original nodes
2. Add to cloned dict if not in
3. Queue to keep the neighbors of the cloned copies
4. End when queue is empty
5. Return the cloned[node] which is the first node

Runtime: O(V + E), Space: O(V)
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # clone each node
        cloned = {}
        cloned[node] = Node(node.val)
        # queue for the neighbors -> entire node with val + neighbors
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                # add to the cloned if not alr there
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # else, add neighbor to the node
                cloned[cur].neighbors.append(cloned[neighbor])
        # queue is empty, went through all nodes
        return cloned[node]
        
            
