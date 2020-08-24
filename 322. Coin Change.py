#  https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], k: int) -> int:
        res = [k + 1] *(k + 1)
        
        res[0] = 0
        
        for i in coins:
            for j in range(i, k + 1):
                res[j] = min(res[j], res[j - i] + 1)
        return res[k] if res[k] != k + 1 else -1
    
    #  Dynamic programming Bottom Up Approach
