#  https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        l = 0
        for i in range(len(arr)):
            if arr[i] != val:
                arr[l] = arr[i]
                l += 1
        return l
