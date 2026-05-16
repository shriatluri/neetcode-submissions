# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Stucture not value
        # [0, n-1, 1, n-2, 2, n-3, 3 ...]
        # get to the middle of the linked list, prev, reverse second half, merge

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the seocnd half of the list, prev.next
        cur = slow.next
        prev = None
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # merge the two
        first, second = head, prev
        while second:
            temp = first.next
            secondtemp = second.next
            first.next = second
            second.next = temp
            first = temp
            second = secondtemp
            

        
            




