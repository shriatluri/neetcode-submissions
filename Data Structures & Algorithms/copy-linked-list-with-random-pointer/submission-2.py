"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Original val, next pointer, randon pointer
        Go through the linked list and store the cur.next and cur.random for each node?
        Return dummy.next

        Method:
        Random pointer will be the challenge, ex: we haven't created the copy of the node that the random pointer will be pointer at

        First pass: Just create the nodes themselves and map OG node to new copy
        Second pass: All the pointer connecting, next and random
        '''
        # to handle when we point to a null value
        oldToCopy = {None : None}

        # first pass: just copy
        cur = head
        while cur:
            # clone of node
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        # second pass: copies
        cur = head
        while cur:
            copy = oldToCopy[cur]
            # map to the copy's we alr created
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        # return the first node in the copy: will return all dict vals
        return oldToCopy[head]
        
        
         
        







            