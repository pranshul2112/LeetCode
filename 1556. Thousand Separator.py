#  https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        
        res = ("{:,}".format(n).replace(",", "."))
        
        
        return res
