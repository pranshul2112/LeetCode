# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            
        ptr1 = nums[0]
        ptr2 = tortoise
        
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            
        return ptr1
