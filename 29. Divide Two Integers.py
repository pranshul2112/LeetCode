#  https://leetcode.com/problems/divide-two-integers/

import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = (dividend/divisor)
        a = (dividend/divisor)
        if a == 0:
            return 0
        if a > 0:
            if a >= 2 ** 31:
                return 2 ** 31 - 1
            return math.floor(a)
        if a <= - 2 ** 31:
            return -2 ** 31 
        return math.ceil(a)    
