# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i
        
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            
            # Pick root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Find position in inorder
            mid = index_map[root_val]
            
            # Build left and right
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)