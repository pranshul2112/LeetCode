#  https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        if arr == []:
            return []
        n = len(arr)
        even = []
        odd = []
        e, o = 0, 0
        for i in range(n):
            if arr[i] % 2 == 0:
                even.append(arr[i])
                
            else:
                odd.append(arr[i])
        res = even + odd
        return res
