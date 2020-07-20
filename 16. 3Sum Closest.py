#  https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        diff = 2 ** 31
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                x = nums[i] + nums[low] + nums[high]
                if abs(x - target) < abs(diff):
                    diff = target - x
                if x < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0:
                return target
                
        return target - diff
   
