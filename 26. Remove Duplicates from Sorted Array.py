#  https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
                
        arr = list(dic.keys())
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)
