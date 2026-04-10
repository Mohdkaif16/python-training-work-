class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        
        # Count frequency
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        result = -1
        
        # Check lucky numbers
        for num in count:
            if num == count[num]:
                result = max(result, num)
        
        return result