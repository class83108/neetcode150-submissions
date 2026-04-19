# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 先找到 linked list 分割點
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 右半邊 linked list 做 reverse
        curr_node = slow.next
        slow.next = None
        prev = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            # 指針往後一格
            prev = curr_node
            curr_node = next_node


        # reorder listed list
        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second 
            second.next = first_next 

            first = first_next
            second = second_next 


        

        


        
            


        