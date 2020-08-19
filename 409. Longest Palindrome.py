#  https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
            
        res, odd_found = 0, False
        
        for key, val in dic.items():
            if val % 2 == 0:
                res += val
            else:
                odd_found = True
                res += val - 1
        if odd_found:
            res += 1
        return res
        
