#  https://leetcode.com/problems/reverse-integer/


# Naive Method 

class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        res = 0
        if x < 0:
            x -= 2 * x
            flag = 1
        while x > 0:
            rem = x % 10
            res = res * 10 + rem
            x //= 10
        if res < - 2 ** 31 or res > 2 ** 31 - 1:
            return 0
        if flag == 0:
            return res
        return -res
      
# Efficent Method 
class Solution:
    def reverse(self, x: int) -> int:
       
        res = int(str(abs(x))[::-1])
        
        return (res if x > 0 else -res) if res.bit_length() < 32 else 0 
