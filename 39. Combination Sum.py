#  https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, arr: List[int], k: int) -> List[List[int]]:
        dp = [[] for _ in range(k + 1)]
        
        for i in arr:
            for j in range(1, k + 1):
                if j < i:
                    continue
                
                if j == i:
                    dp[j].append([i])
                    #  print(dp[j], end=" ")
                else:
                    for a in dp[j - i]:
                        dp[j].append(a +[i])
                        #  print(dp[j], end=" ")
        return dp[-1]
