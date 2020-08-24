#  https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr, k: int):
        n = len(arr)
        if n == 0:
            return 0
        res = [0] * n

        max_interval = arr[0]
        for i in range(k):
            max_interval = max(max_interval, arr[i])
            res[i] = (i + 1) * max_interval
        #print(res)
        # recursively
        for i in range(k, n):
            tmp = 0
            max_interval = arr[i]
            for j in range(1, k + 1):
                tmp = max(tmp, j * max_interval + res[i - j])
                max_interval = max(max_interval, arr[i - j])
            res[i] = tmp
        return res[-1]
