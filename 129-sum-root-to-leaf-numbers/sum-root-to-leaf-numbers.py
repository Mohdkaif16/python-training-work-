class Solution:
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0

            current = current * 10 + node.val

            # if leaf node → return number
            if not node.left and not node.right:
                return current

            # recurse left + right
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)