# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # traverse through the entire tree (run a bfs or dfs)
        # do a dfs( to get height of that root and then)
        # get the max of the heights through out the entire tree
        # return that max value

        maxDiameter = 0
        def height(root):
            
            if not root:
                return -1

            leftHeight = height(root.left)
            rightHeight = height(root.right)
            
            diameter = leftHeight + rightHeight  + 2
            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, diameter)

            return max(leftHeight,rightHeight) + 1
        
        # def dfs(root):
        #     if not root:
        #         return
            
        #     diameter = height(root.left) + height(root.right) + 2
        #     print(diameter)
        #     nonlocal maxDiameter
        #     maxDiameter = max(diameter, maxDiameter)

        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        height(root)
        return maxDiameter