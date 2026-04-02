class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def solve(nums):
            if len(nums) == 0:
                return [[]]
            small = solve(nums[1:])
            ans = []
            for lst in small:
                ans.append(lst)
                ans.append([nums[0]] + lst)
            return ans
        result = solve(nums)
        final = []
        for x in result:
            if x not in final:
                final.append(x)
        return final
