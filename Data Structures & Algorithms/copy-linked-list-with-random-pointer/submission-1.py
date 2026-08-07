"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        memo,curr = {}, head
        while curr: memo[curr] = Node(curr.val); curr = curr.next #mapping the original nodes with the copy nodes (with the proper value)
        curr = head
        while curr and curr.next: memo[curr].next = memo[curr.next]; curr = curr.next #assigning copies of the hashmap the proper .next pointer
        for org in memo:
            memo[org].random = memo.get(org.random, None)

        return memo[head]
        