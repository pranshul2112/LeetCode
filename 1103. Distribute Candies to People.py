#  https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num: int) -> List[int]:
        res = [0] * num
        i = 0
        cycle = 1
        while candies > 0:
            
            if cycle > candies:
                res[i] += candies
            else:
                res[i] += cycle
            i += 1
            if i == num:
                i = 0
                
            
            candies -= cycle
            cycle += 1
       
        return res
