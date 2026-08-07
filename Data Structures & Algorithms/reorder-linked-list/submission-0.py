# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle node
        fast, slow, left = head, head, head
        while fast and fast.next: slow = slow.next; fast = fast.next.next
        # separate to two halves
        second = slow.next
        slow.next = None
        
        # 2. reverse the second half of list
        right = None
        while second:
            old_second = second.next
            second.next = right
            right = second
            second = old_second
        # 3 merging the two
        while right and left:
            old_left = left.next
            old_right = right.next
            
            left.next = right
            right.next = old_left
            
            left = old_left
            right = old_right
    
            # old_left = left.next
            # old_right = right.next
            # left.next = right
            # left = old_left
            # right.next = left
            # right = old_right
    
            