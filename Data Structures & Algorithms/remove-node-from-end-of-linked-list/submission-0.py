# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #dummy node set to 0 (doesn't matter) and next is the head of the list
        dummy = ListNode(0, head)
        left = dummy 
        right = head
        #right set until it is head + n
        while n > 0 and right:
            right = right.next
            n -= 1
        #until right reaches null, keep shifting
        while right:
            left = left.next
            right = right.next
        #reassign value (delete node)
        left.next = left.next.next
        return dummy.next