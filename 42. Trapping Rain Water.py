# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        n = len(height)
        left, right = [0] * n, [0] * n
        maxwater, totalwater = 0, 0
        
        for i in range(n):
            maxwater = max(maxwater, height[i])
            left[i] = maxwater
            
        maxwater = 0
        
        for i in range(n - 1, -1, -1):
            maxwater = max(maxwater, height[i])
            right[i] = maxwater
            
        for i in range(n):    
            totalwater += min(left[i], right[i]) - height[i]
            
        return totalwater
        
