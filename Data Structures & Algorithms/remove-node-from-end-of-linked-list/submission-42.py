# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = dummy
        checkAhead = dummy

        if not head.next:
            return None

        for _ in range(n):
            checkAhead = checkAhead.next
        
        while checkAhead.next:
            temp = temp.next
            checkAhead = checkAhead.next
        
        temp.next = temp.next.next

        return dummy.next
        

