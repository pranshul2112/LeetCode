#  https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        n = len(arr)
        if k > n:
            return 0
        s = 0
        for i in range(k):
            s += arr[i]
        max_s = s

        for i in range(k, n):
            s += arr[i] - arr[i-k]
            if s > max_s:
                max_s = s
            

        return max_s / k
