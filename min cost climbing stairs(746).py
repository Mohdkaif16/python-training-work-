class Solution:
    def minCostClimbingStairs(self, cost):
        prev = 0
        curr = 0
        for c in cost:
            new = min(prev, curr) + c
            prev = curr
            curr = new
        return min(prev, curr)
