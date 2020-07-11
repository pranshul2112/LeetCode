#  https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution(object):
    def longestPalindromeSubseq(self, s):
        map = {}
        def find(s):
            if s not in map:
                max_len = 0
                for x in set(s):
                    i, j = s.find(x), s.rfind(x)
                    max_len = max(max_len, 1 if i == j else 2 + find(s[i + 1 : j]))
                map[s] = max_len
            return map[s]
        return find(s)
        
