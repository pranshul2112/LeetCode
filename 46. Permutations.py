#  https://leetcode.com/problems/permutations/

import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = list(itertools.permutations(nums))
        return arr
