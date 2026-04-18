# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_node, prev_node = head, None

        while curr_node:
            # 將 next_node 儲存到變數
            next_node = curr_node.next

            # 將 curr 指回前一個 node
            curr_node.next = prev_node
            
            # 指到後面一組
            prev_node = curr_node
            curr_node = next_node
            
        
        return prev_node
        