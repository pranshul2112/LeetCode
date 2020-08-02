#  https://leetcode.com/problems/plus-one/


#  Solution One
class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        i = len(nums) - 1
        while i > -1:
            if nums[i] == 9:
                nums[i] = 0
            else:
                nums[i] += 1
                return nums
            i -= 1
            
        return [1] + nums
         
         
#  Solution Two
class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        res = int("".join(str(c) for c in nums))
        res += 1
        res = str(res)
        return list(res)
            
