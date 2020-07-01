#  https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        flag = j = i = 0
        while j < len(s):
            if s[j] in map and i <= map[s[j]]:

                i = map[s[j]] + 1

            else :
                flag = max(flag, j - i + 1)
            map[s[j]] = j
            j += 1
            
        return flag
