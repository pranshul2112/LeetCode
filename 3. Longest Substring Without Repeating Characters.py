#  https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = longest_so_far = cur_start = 0
        seen = {}
        
        for i, letter in enumerate(s):
            
            if letter in seen and seen[letter] >= cur_start:
                cur_start = seen[letter] + 1
                cur_len = i - seen[letter]
                seen[letter] = i   
            else:
                seen[letter] = i
                cur_len += 1
                longest_so_far = max(longest_so_far, cur_len)
                
        return longest_so_far
                
                
