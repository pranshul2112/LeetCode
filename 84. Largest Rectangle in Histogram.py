#  https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        if arr == []:
            return 0
        
        if len(arr) == 1:
            return arr[0]
        stack = []
        res = 0
        for i, h in enumerate(arr):
            start = i
            
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                
                start = index
                
            stack.append((start, h))
            
            
        for i, h in stack:
            res = max(res, h * (len(arr) - i))

        return res
        
        
