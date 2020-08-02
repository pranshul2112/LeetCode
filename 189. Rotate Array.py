#  https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        rf = k % n
        
        i = j = 0
        while j < n:
            curr, pre = i, arr[i]
            while True:
                nex = (rf + curr) % n
                arr[nex], pre = pre, arr[nex]
                curr = nex
                j += 1
                if i == curr:
                    break
            i += 1
            
        
