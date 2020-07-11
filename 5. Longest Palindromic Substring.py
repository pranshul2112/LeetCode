#  https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        mem = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(mem) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    mem = s[i:j]
                    break
        return mem
