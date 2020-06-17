#  https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        right = 1
        count = set()
        
        while left < right and right < len(nums):
            if nums[right] - nums[left] == k:
                count.add((nums[left], nums[right]))
                left += 1
                right = left + 1
                
            elif nums[right] - nums[left] > k:
                left += 1
                right = left + 1
            else :
                right += 1
                
        return len(count) 
