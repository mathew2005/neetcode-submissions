# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # input: root (non-empty bt)
        # output: max path sum
        
        # node can appear at most once in a sequence
        # path doesn't necessarily have to include the root

        # value can be negative too (so keep that in mind) (so it might be better to have less length of nodes when the values are negative)
        
        maxPath = float('-inf')

        def pathSum(root):
            if not root:
                return 0
            
            leftPath = max(0, pathSum(root.left))
            rightPath = max(0,pathSum(root.right))

            nonlocal maxPath
            maxPath = max(maxPath, leftPath + rightPath + root.val)

            return root.val + max(leftPath, rightPath)

        
        pathSum(root)
        return maxPath