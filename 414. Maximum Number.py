#  https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, arr: List[int]) -> int:
        arr = list(set(arr))
        arr = [i * (-1) for i in arr]

        heapq.heapify(arr)

        if len(arr) < 3:
            return -arr[0]
        else:
            heapq.heappop(arr)
            heapq.heappop(arr)
            return -arr[0]
