# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]

        r = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= r
            r *= nums[i]

        return output
