# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Return type should be a node
        ex: 123 + 456 will be 321 + 654 so that means 1 and 4 will be the ones place
        Need to be able to do in-place addition with the nodes and have a carry value
        '''
        dummy = ListNode()
        cur = dummy

        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # current value
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10 # digit without the carry
            cur.next = ListNode(val)

            # increment pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            
