#  https://leetcode.com/problems/next-permutation/

class Solution:
    def swap(self, nums, a, b):
        nums[a] += nums[b]
        nums[b] = nums[a] - nums[b]
        nums[a] -= nums[b]

    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            self.swap(nums, 0, 1)
            return
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1

        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return
        next_val = dec + 1
        while next_val < len(nums) and nums[next_val] <= nums[dec]:
            next_val += 1

        self.swap(nums, next_val, dec)
