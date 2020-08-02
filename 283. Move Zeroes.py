#  https://leetcode.com/problems/move-zeroes/


#  Beats 90% in time complexity
class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if arr == []:
           return []
        i = 0
        for j in range(len(arr)):
            if arr[j] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
     
#  Beats 90% in space complexity
class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if arr == []:
           return []
        i, j = 0, 1
        while i < j and j < len(arr):
            if arr[i] != 0:
                i += 1
                j = i + 1
            elif arr[i] == 0 and arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j = i + 1
            else:
                j += 1
                
        
