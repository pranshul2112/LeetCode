#  https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #  If empty head    
        if not head:
            return []


        #  To reorder a linked list, we follow three steps
        
        
        #  Step 1: Find the middle element
        slow, fast = head, head
        #  We use Floyd's tortoise and hare algorithm in which one pointer traverses twice as fast as the other

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        #  Step 2: Reverse the second half
        pre, cur = None, slow.next

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        slow.next = None  #  This avoids a cycle in the linkedlist


        #  Step 3:  Merge first and second half

        head1, head2 = head, pre
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp

        
        #  Finally return
        return head

    
