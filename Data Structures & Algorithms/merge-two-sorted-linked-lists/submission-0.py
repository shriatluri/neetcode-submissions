# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                #add value to tail
                tail.next = list1
                #increment
                list1 = list1.next
            else:
                #add value to tail
                tail.next = list2
                #increment
                list2 = list2.next
            #increment tail
            tail = tail.next
        #if one list is empty
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        #return head of the merged list
        return dummy.next