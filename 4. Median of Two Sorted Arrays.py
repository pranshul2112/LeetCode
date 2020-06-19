#  https://leetcode.com/problems/median-of-two-sorted-arrays/

from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        
        return statistics.median(arr)
