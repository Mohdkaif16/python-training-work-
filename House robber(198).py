# using temp veriable for storage 
class Solution:
    def rob(self, nums):
        p = 0   
        c = 0   
        for n in nums:
            temp = c              
            c = max(c, p + n)  
            p = temp              
        return c 
# without using temp veriable 
class Solution:
    def rob(self, nums):
        a, b = 0, 0
        
        for n in nums:
            a, b = b, max(b, a + n)
        
        return b
