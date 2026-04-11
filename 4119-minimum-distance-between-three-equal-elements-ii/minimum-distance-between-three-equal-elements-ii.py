class Solution:
    def minimumDistance(self, nums):
        pos = {}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        ans = float('inf')
        for indices in pos.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                d = 2 * (indices[i+2] - indices[i])
                if d < ans:
                    ans = d
        if ans != float('inf'):
            return ans
        else :
            return -1           