# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        def return_tail_node_and_remove_prev_node_next(node):
            while node.next:
                if node.next.next == None:
                    tail_node = node.next
                    node.next = None
                    return tail_node
                else:
                    node = node.next
            return None

        
        while head.next:

            next_node = head.next
            if head.next.next != None:
                tail_node = return_tail_node_and_remove_prev_node_next(head)
                head.next = tail_node
                tail_node.next = next_node
                head = next_node
            else:
                return

            


        