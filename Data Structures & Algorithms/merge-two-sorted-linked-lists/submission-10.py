# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node is the key here
        # if one list is done, just add the remaining portion of the other to the dummy node
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        # add to end
        if list1:
            node.next = list1
        else:
            node.next = list2
        return dummy.next

        
        
