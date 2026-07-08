# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # input: root, subroot
        # output: boolean (if subroot exists in root -> True else False)
        if not subRoot:
            return True
        
        def isSameTree(root,subRoot):
            if root and not subRoot:
                return False
            if not root and subRoot:
                return False
            
            if not root:
                return True

            if root.val == subRoot.val:
                return isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right)
            else:
                return False

        def dfs(root, subRoot):
            if not root:
                return False
            
            if root.val != subRoot.val:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
            else:
                return isSameTree(root, subRoot) or dfs(root.left,subRoot) or dfs(root.right, subRoot)
        
        return dfs(root,subRoot)