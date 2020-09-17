#  https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        
        
        def generateArray(a):
            res = [0] * 26
            
            for i in a:
                res[ord(i) - ord("a")] += 1 
                
            return res
        
        
        pmap = generateArray(p)
        smap = generateArray(s[:len(p)])
        
        res = []
        if pmap == smap:
            res.append(0)
            
        for i in range(len(p), len(s)):
            smap[ord(s[i]) - ord("a")] += 1
            
            smap[ord(s[i - len(p)]) - ord("a")] -= 1
           # print(smap)
            if smap == pmap:
                res.append(i - len(p) + 1)
        return res
