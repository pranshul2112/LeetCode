#  https://leetcode.com/problems/rectangle-overlap/

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #  rec1 = [x1, y1, x2, y2]
        #  rec2 = [x1, y1, x2, y2]
        
        
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
            return False
        
        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False
        
        return True 

