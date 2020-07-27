#  https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x = y = float("inf")
        
        for i in range(len(nums)):
            if nums[i] <= x:
                x = nums[i]
            elif nums[i] <= y:
                y = nums[i]
            else:
                return True
        return False 
