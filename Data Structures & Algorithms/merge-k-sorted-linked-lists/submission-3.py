# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0 or lists == [None] :
            return None
        # [A,B,C,D,E,F,G]
        while len(lists) > 1:
            res = []
            for i in range(0,len(lists), 2):
                if i + 1 < len(lists):
                    res.append(self.mergeTwoLists(lists[i], lists[i+1]))
                else:
                    res.append(lists[i])
            lists = res

        return res[0]
    

    def mergeTwoLists(self,list1, list2):
        tail = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next