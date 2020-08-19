#  https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:   return None
        
        
        ap = headA
        bp = headB
        
        
        while ap != bp:
            
            ap = headB if ap == None else ap.next
            bp = headA if bp == None else bp.next
            
        return ap
        
