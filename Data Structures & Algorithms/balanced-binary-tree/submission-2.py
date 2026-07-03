# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # input: bt
        # output: boolean 
        # condition: height-balanced (diff (left and right) <= 1)
        # edge cases: empty state, one node, 
        # sanity check: skewed tree
        # keep in mind: abs()

        # solution 1
        # base case (if not root) => return true
        if not root:
            return True
        
        # do a dfs height retriever on leftroot and rightroot (return leftHeight and rightHeight)
        def dfsHeight(root: Optional[TreeNode]):
            # base case
            if not root: 
                return (0, True)
            leftHeight, left_balanced = dfsHeight(root.left)
            rightHeight, right_balanced = dfsHeight(root.right)
            return (max(leftHeight, rightHeight) + 1,  left_balanced and right_balanced and abs(leftHeight - rightHeight) <= 1)
        #  run the dfs on both the leftroot(root.left) and rightroot (root.right)
        
        # TIME O(n), Space: O(n)
        return dfsHeight(root)[1]