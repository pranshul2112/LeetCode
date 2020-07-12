#  https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]
