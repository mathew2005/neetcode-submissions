# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def BT(preorder, inorder, root):
                
            if not inorder and not preorder:
                return None

            mid = inorder.index(preorder[0])
            root = TreeNode(preorder[0])

            root.left = BT(preorder[1:mid+1], inorder[:mid], root)
            root.right= BT(preorder[mid+1:], inorder[mid+1:], root)

            return root
        return BT(preorder, inorder, None)
        