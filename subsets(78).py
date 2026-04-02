class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        smallOutput = self.subsets(nums[1:])
        output = []   
        for lst in smallOutput:
            output.append(lst)
            output.append([nums[0]] + lst)
        return output
