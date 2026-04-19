# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        while root:
            
            # both in left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # both in right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            else:
                return root   # split point → LCA