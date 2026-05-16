# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        curr = head
        temp = None

        while curr:
            tempNext = curr.next
            curr.next = newHead
            newHead = curr
            curr = tempNext
        
        return newHead
        
        
            



            



