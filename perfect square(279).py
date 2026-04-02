class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n #float("inf") where inf is infinity . In DP, we want to find the minimum value So we start with a very large number so that any real answer becomes smalle.
                                      #We don’t know the answer → set it to infinity as defulte .
        for i in range(1, n + 1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]
