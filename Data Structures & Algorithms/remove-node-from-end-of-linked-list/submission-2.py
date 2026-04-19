# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 1
        while curr:
            curr = curr.next
            if curr:
                count += 1
        
        
        remove_node_index = count - n + 1

        curr, prev = head, None
        count = 1
        

        while curr:
            next_node = curr.next
            
            # 還沒遇到要去除的話
            if count < remove_node_index:
                prev = curr
                curr = next_node
                count += 1
            # 遇到我們要去除的點
            elif count == remove_node_index:
                curr.next = None
                if prev:
                    
                    prev.next = next_node

                # 如果第一個點就是要去除的點呢？
                else:
                    head = next_node
                break
            else:
                break

        return head
            
            
            
            

        

