# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, remaining_sum):
            if not node:
                return
            new_path = path + [node.val]
            remaining_sum -= node.val
            if not node.left and not node.right:
                if remaining_sum == 0:
                    result.append(new_path)
                return
            
            dfs(node.left, new_path, remaining_sum)
            dfs(node.right, new_path, remaining_sum)

        dfs(root, [], targetSum)
        return result