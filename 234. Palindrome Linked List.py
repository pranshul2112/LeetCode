#  https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, root):
        pre = None
        cur = root
        
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        return pre
        
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        slow = self.reverseList(slow)
        
        fast = head
        
        while slow:
            if fast.val != slow.val:
                return False
            
            fast = fast.next
            slow = slow.next
            
        return True
    
    
