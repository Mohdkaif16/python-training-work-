# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        
        # Helper to find middle node
        def findMiddle(head):
            prev = None
            slow = head
            fast = head
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            # Disconnect left half
            if prev:
                prev.next = None
            
            return slow
        
        # Base case
        if not head:
            return None
        
        # Find middle
        mid = findMiddle(head)
        
        # Create root
        root = TreeNode(mid.val)
        
        # If only one node
        if head == mid:
            return root
        
        # Recursively build
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root