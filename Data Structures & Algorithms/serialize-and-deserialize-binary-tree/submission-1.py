# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        inorderList = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            inorderList.append(str(root.val))
            inorder(root.right)
       
        inorder(root)
        
        preorderList = []
        
        def preorder(root):
            if not root:
                return 
            
            preorderList.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        inorderStr = ",".join(inorderList)
        preorderStr = ",".join(preorderList)
        
        return inorderStr + ":" + preorderStr
        

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inorder, preorder = data.split(":")
        inorder, preorder = inorder.split(","), preorder.split(",")
        print(inorder, preorder)
        def dfs(inorder,preorder):
            if not inorder and not preorder:
                return None
            
            
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = dfs(inorder[:mid], preorder[1:mid+1])
            root.right = dfs(inorder[mid+1:], preorder[mid+1:])
            return root

        dfs(inorder,preorder)

        return root