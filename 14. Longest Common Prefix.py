#  https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            
            if strs == []:
                return ""
            res = ""
            n = len(min(strs))
            for i in range(n):
                flag = 1
                for j in range(len(strs)):
                    if j == 0:
                        test = strs[j][i]

                    else:
                        if test != strs[j][i]:
                            flag = 0
                            break
                if flag:
                    res = res + test

                else:
                    break
            return res
