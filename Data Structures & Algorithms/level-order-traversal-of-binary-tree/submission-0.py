from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs -> (level by level)
        # how do we know which level we are at?
        # input: bt
        # output: list containing sublists (of values of each nodes from l to r)
        # edge cases: one node, null, skewwed tree

        # time complexity: O(n)
        # space complexity: O(n)

        if not root:
            return []
        # setup queue (intialized with root inside)
        q, result = deque([root]), []
        # keep looping until queue is empty
        while q:
            sublist = []
            for _ in range(len(q)):
                curr = q.popleft()
                sublist.append(curr.val)
                # add left node to queue if it exists
                if curr.left:
                    q.append(curr.left)
                # add right node to queue if it exists 
                if curr.right:
                    q.append(curr.right)
                
            result.append(sublist)
        return result


"""
q = [1]

"""