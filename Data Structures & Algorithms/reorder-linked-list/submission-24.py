# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        # reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        while prev:
            temp = head.next
            secondTemp = prev.next
            head.next = prev
            prev.next = temp
            head = temp
            prev = secondTemp

        

        

