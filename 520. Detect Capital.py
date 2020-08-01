#  https://leetcode.com/problems/detect-capital/  

class Solution:
    def detectCapitalUse(self, s: str) -> bool:
        if len(s) == 1:
            return True
        firstisuppper = False
        if s[0].isupper():
            firstisuppper = True
        if firstisuppper:
            
            if s[1].isupper():
                i = 2
                while i < len(s):
                    if s[i].islower():
                        return False
                    i += 1
                return True
            else:
                i = 2
                while i < len(s):
                    if s[i].isupper():
                        return False
                    i += 1
                return True
    
        else:
            i = 1
            while i < len(s):
                if s[i].isupper():
                    return False
                i += 1
            return True
