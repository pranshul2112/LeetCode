#  https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, arr):
        arr.sort()
        res = []
        for i in range(len(arr) - 2):
            if i == 0 or (i > 0 and arr[i] != arr[i - 1]):
                low = i + 1
                high = len(arr) - 1
                target = 0 - arr[i]
                while low < high:
                    if arr[low] + arr[high] == target:
                        res.append([arr[i], arr[low], arr[high]])
                        while low < high and arr[low] == arr[low + 1]: low += 1
                        while low < high and arr[high] == arr[high - 1]: high -= 1
                        low += 1
                        high -= 1
                    elif arr[low] + arr[high] > target:
                        high -= 1
                    else:
                        low += 1
                        
        return res
    
