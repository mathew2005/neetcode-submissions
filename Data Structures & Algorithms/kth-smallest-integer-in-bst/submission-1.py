# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # input: bst, k(int)
        # output: kth smallest val (1-indexed)
        

        # base case: 
        # null -> return 0
        result = []
        def inorder(root):
            if not root:
                return 
        
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return result[k-1] 