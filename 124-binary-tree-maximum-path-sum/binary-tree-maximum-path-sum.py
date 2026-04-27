class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # get max path from left and right
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # case 1: path through current node (split path)
            current_sum = node.val + left + right

            # update global max
            self.max_sum = max(self.max_sum, current_sum)

            # case 2: return one side (no split)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum