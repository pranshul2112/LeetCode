#  https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set()
        for i in range(len(edges)):
            res.add(edges[i][1])
        
        ans = []
        for i in range(n):
            if i not in res:
                ans.append(i)
        return ans
        
