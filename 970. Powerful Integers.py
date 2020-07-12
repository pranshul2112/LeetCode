#  https://leetcode.com/problems/powerful-integers/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i, j = 0, 0
        res = set()
        temp_x = x ** i
        temp_y = y ** j
        while temp_x < bound:
            while temp_x + temp_y <= bound:
                res.add(temp_x + temp_y)
                j += 1
                temp_y = y ** j
                if y == 1:
                    break
            i += 1
            temp_x = x ** i
            if x == 1:
                break
            j = 0
            temp_y = y ** j
        
        return list(res)
