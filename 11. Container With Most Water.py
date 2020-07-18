#  https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, arr):
        left, right, area = 0, len(arr) - 1, 0
        while left < right:
            area = max(area, (right - left) * min(arr[left], arr[right]))
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return area
