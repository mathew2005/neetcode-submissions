# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # input: BST, (node values are unique), nodes p and q
        # return :LCA of p andq (node) or node.val (???)
        # ancestor can be descendant of itself (lowest node => least amount of nodes that contains p and q)
        
        # case 1: we don't find p and q
        # case 2: we find p but not q
        # case 3: we find both p and q


        # 5  : 3,8,1,4,7,9,2
        # 3 : 1,4,2
        # 1: 2
        # 4: []
        # 8: 7
        # 9: []

        # bfs with hashmap building
        # run through hashmap (finding nodes that contain p and q)
        # time : O(n^2)
        # space: O(n)
        curr = root
        print(curr.val)
        while curr:
            # CASE 0 : p or q == curr.val
            if p == curr.val or q == curr.val:
                # return curr.val
                return curr.val

            # CASE 1: p.val is in Left and q.val is in Left
            elif p.val < curr.val and q.val < curr.val:
                # go to left
                curr = curr.left
            # CASE 2: p.val is in Right and q.val is in Right
            elif p.val > curr.val and q.val > curr.val:
                # go to right
                curr = curr.right
            # CASE 3: p.val is in Left and q.val is in Right
            else: 
                return curr


