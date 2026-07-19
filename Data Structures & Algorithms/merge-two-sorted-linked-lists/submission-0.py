# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # input: list1 and list2 (sorted)
        # output: head of merged list (should be sorted)
        # assumption: val of nodes is int


        # edge cases: empty linked list, different length, negative values, 
        combined = ListNode()
        curr = combined

        while list1 or list2:

            if not list1 and list2:
                curr.next = ListNode(list2.val)
                curr= curr.next
                list2 = list2.next
            elif not list2 and list1:
                curr.next = ListNode(list1.val)
                curr= curr.next
                list1 = list1.next
            
            elif list1.val < list2.val:
                curr.next = ListNode(list1.val)
                curr= curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr= curr.next
                list2 = list2.next
                

            
        return combined.next