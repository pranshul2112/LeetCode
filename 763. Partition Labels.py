#  https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {c : i for i, c in enumerate(s)}
        #print(dic)
        
        res, m, size = [], -1, 1
        
        for i, c in enumerate(s):
            m = max(m, dic[c])
            if i == m:
                res.append(size)
                size = 1
            else:
                size += 1
        return res
