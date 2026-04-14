class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        duplicate = -1

        for num in nums:
            if num in s:
                duplicate = num
            s.add(num)

        for i in range(1, n + 1):
            if i not in s:
                missing = i
                break

        return [duplicate, missing]