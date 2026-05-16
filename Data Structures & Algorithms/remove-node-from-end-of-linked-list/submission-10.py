# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove element in len(list) - n index and return head
        # dummy node, will point to head while we make the changes, we make the change return dummy
        # for a one pass solution, have two pointer on at the head and one at index n + 1
        dummy = ListNode(0, head)
        # which index they start at, dummy
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
        