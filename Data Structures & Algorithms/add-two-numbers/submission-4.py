# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # s1 = []
        # s2 = []

        # while l1:
        #     s1.append(l1.val)
        #     l1 = l1.next
            

        # while l2:
        #     s2.append(l2.val)
        #     l2 = l2.next

        # d1 = 0
        # d2 = 0

        # s3 = []
        # count = 0
        # while d1 < len(s1) or d2 < len(s2):
            
        #     if d1 >= len(s1) and d2 < len(s2):
        #         s3.append((s2[d2]+ count) % 10)
        #         count = (s2[d2] + count) // 10
        #         d2 += 1
        #         continue
        #     if d2 >= len(s2) and d1 < len(s1):
        #         s3.append((s1[d1]+ count) % 10)
        #         count = (s1[d1] + count) // 10
        #         d1 += 1
        #         continue
            
            
        #     s3.append((s1[d1] + s2[d2]+ count) % 10)
        #     count = (s1[d1] + s2[d2] + count) // 10

        #     d2 += 1
        #     d1 += 1
        
        # if count:
        #     s3.append(count)
        
        # l3 = ListNode()
        # curr = l3
        # for num in s3:
        #     curr.next = ListNode(num)
        #     curr = curr.next
        # return l3.next
        l3 = ListNode() 
        curr = l3
        count = 0
        while l1 or l2:
            if l1 and not l2:
                curr.next = ListNode((l1.val + count) % 10)
                count = (l1.val + count) // 10
                l1 = l1.next
            elif not l1 and l2:
                curr.next = ListNode((l2.val + count) % 10)
                count = (l2.val + count) // 10
                l2 = l2.next
            
            else:
                curr.next = ListNode((l1.val + l2.val + count) % 10)
                count = (l1.val + l2.val + count) // 10
                l1,l2 = l1.next, l2.next
            
            
            curr = curr.next
            
            
        
        if count:
            curr.next = ListNode(count)
        
        return l3.next

