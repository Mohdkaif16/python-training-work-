# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(left, right):
            # Both null → symmetric
            if not left and not right:
                return True
            
            # One null → not symmetric
            if not left or not right:
                return False
            
            # Check value + mirror children
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)