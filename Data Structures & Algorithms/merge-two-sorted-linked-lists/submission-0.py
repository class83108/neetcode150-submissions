# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr_node = dummy

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            
            if val1 < val2:
                curr_node.next = list1
                list1 = list1.next
            elif val1 > val2:
                curr_node.next = list2
                list2 = list2.next
            else:
                curr_node.next = list1
                list1 = list1.next
            curr_node = curr_node.next

        if list1:
            curr_node.next = list1
        
        if list2:
            curr_node.next = list2
        
        return dummy.next