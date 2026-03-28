# using temp veriable for storage 
class Solution:
    def rob(self, nums):
        prev = 0   
        curr = 0   
        for n in nums:
            temp = curr              
            curr = max(curr, prev + n)  
            prev = temp              
        return curr 
# without using temp veriable 
class Solution:
    def rob(self, nums):
        a, b = 0, 0
        
        for n in nums:
            a, b = b, max(b, a + n)
        
        return b
