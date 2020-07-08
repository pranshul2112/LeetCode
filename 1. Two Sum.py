#  https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        map = {}
        for key, val in enumerate(arr):
            if target - val in map:
                return [map[target - val], key]
            else:
                map[val] = key
        
