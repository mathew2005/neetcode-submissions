# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case: if null -> return True
        def isValidSubBST(root: Optional[TreeNode], lb = float('-inf'), rb = float('inf')):
            if not root:
                return True
            
            if not (lb < root.val and root.val < rb):
                return False
            
            return isValidSubBST(root.left,lb,root.val) and isValidSubBST(root.right,root.val,rb)
            
        return isValidSubBST(root)