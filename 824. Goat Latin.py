#  https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        def abc(i, string):
            if string[0] not in "AEIOUaeiou":
                string = string[1:] + string[0]
            
            return string + "ma" + ("a" * i)
        
        return " ".join([abc(i, w) for i, w in enumerate(S.split(), 1)])
    
            
