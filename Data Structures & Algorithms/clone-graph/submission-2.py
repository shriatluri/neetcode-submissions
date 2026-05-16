"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        bfsQueue = deque()
        result = {}

        bfsQueue.append(node)
        result[node] = Node(node.val)

        while bfsQueue:
            currNode = bfsQueue.popleft()

            for neighbor in currNode.neighbors:
                if neighbor not in result:
                    bfsQueue.append(neighbor)
                    result[neighbor] = Node(neighbor.val)
                result[currNode].neighbors.append(result[neighbor])
        
        return result[node]
                

