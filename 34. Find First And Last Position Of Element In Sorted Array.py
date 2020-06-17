#  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        indexstart = -1
        indexend = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            midpoint: int = left + (right - left) // 2
            if nums[midpoint] >= target:
                right = midpoint - 1
            else:
                left = midpoint + 1

            if nums[midpoint] == target:
                indexstart = midpoint


        left = 0
        right = len(nums) - 1
        while left <= right:
            midpoint: int = left + (right - left) // 2
            if nums[midpoint] <= target:
                left = midpoint + 1
            else:
                right = midpoint - 1

            if nums[midpoint] == target:
                indexend = midpoint


        return [indexstart, indexend]
        

