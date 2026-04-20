# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        dummy = head
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10

            next_node = ListNode(val=value)
            dummy.next = next_node

            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return head.next
        