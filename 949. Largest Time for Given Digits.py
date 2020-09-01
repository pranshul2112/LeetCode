#  https://leetcode.com/problems/largest-time-for-given-digits/


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        arr = sorted(A, reverse=True)
        #print(arr)
        arr = list(itertools.permutations(arr))
        #print(arr)
        for h1, h2, m1, m2 in arr:
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            
            if hour < 24 and minute < 60:
                return f"{h1}{h2}:{m1}{m2}"
            
            
        return ""
