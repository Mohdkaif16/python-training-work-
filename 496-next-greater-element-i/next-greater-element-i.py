class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        stack = []
        next_greater = {}
        
        # Process nums2
        for num in nums2:
            
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            
            stack.append(num)
        
        # Remaining elements → no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Build result for nums1
        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result