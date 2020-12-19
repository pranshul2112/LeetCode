#  https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        for i in range(1, n + 1):
            ans = ""
            if i % 3 == 0:
                ans = ans + "Fizz"
                
            if i % 5 == 0:
                ans = ans + "Buzz"
                
            if ans == "":
                res.append(str(i))
            else:
                res.append(ans)
            
        return res
