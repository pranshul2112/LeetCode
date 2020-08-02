#  https://leetcode.com/problems/contains-duplicate/


#  First Solution includes the use of sets and use its properties (slightly faster)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True
            
            
#  Second Solution would be to sort the list and iterate through it, if found a duplicate return "True" otherwise "False"
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
