# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []

        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        
        
        i = len(result) - 1
        
         
        new = ListNode(0)
        curr = new
        while i >= 0:
            curr.next = ListNode(result[i])
            curr = curr.next
            i -= 1    
            
        return new.next