class Solution:
    def rob(self, nums:list[int])->int:
        def helper(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(
            helper(nums[:-1]),
            helper(nums[1:]))
