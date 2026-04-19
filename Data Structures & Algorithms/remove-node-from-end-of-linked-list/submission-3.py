# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 避免我們要清除 node 是第一個
        dummy = ListNode()

        dummy.next = head

        left = right = dummy

        for _ in range(n):
            right = right.next
            if not right:
                return head
        
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


        
        
        
            
            
            
            

        

