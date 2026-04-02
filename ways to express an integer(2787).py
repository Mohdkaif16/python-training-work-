class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        nums = []
        i = 1
        while i ** x <= n:
            nums.append(i ** x)
            i += 1
        def solve(i, remaining):
            if remaining == 0:
                return 1
            if i == len(nums) or remaining < 0:
                return 0
            take = solve(i + 1, remaining - nums[i])
            skip = solve(i + 1, remaining)
            return take + skip
        return solve(0, n)
