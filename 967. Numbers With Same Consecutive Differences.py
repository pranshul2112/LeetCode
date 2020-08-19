#  https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        res = []
        
        def dfs(i, num):
            if num == 0:
                res.append(i) 
                return 
            
            last = i % 10
            
            if last >= k:  dfs(i * 10 + last - k, num - 1)
            if k > 0 and last + k <= 9:  dfs(i * 10 + last + k, num - 1)
            
                
        for i in range(1, 10):
            dfs(i, n -1)
            
        return res
