#  https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, n: int) -> List[int]:
        res = []
        
        for i in range(1, n + 2):
            s = 1
            temp = []
            for j in range(1, n + 2):
                temp.append(s)
                s = s * (i - j) // j
            res.append(temp)
        return res[len(res) - 1]
