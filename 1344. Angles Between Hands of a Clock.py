#  https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, h: int, m: int) -> float:
        #  total = 360 degrees
        #  one hour = 30 degrees
        #  one minute = 6 degrees
        if h == 12:
            h = 0
        if m == 60:
            m = 0
            h += 1
            if h > 12:
                h -= 12
        h = (h * 60 + m) * 0.5
        m *= 6
        angle = abs(h - m)
        return min(angle, 360 - angle)
        
