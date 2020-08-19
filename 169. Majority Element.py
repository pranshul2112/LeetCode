#   https://leetcode.com/problems/majority-element/


#  This algorithm is known as  Boyer-Moore Voting Algorithm and has a runtime complexity of O(n).

class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        c = 0
        candidate = None
        
        for i in arr:
            if c == 0:
                candidate = i
            c += 1 if i == candidate else -1
            
        return candidate
