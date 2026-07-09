# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = ri    ght

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # input: bt
        # x -> good (from root to node x, all nodes <= x)
        # output: number of good nodes (int)
        
            
        def dfs(root,maxEl = float('-inf')):
                
            if not root:
                return 0

            if root.val >= maxEl:
                maxEl = root.val
                return dfs(root.left, maxEl) + dfs(root.right,maxEl) + 1
            else:
                return dfs(root.left, maxEl) + dfs(root.right, maxEl)

        return dfs(root.left, root.val) + dfs(root.right, root.val) + 1
        