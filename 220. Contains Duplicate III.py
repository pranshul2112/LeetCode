#  https://leetcode.com/problems/contains-duplicate-iii/


#  IMPLEMENTATION 1
#  Given below is an implementation in O(n log (k))
#  The idea here is to use inbuilt library function that sorts the data in it for a given range 

from sortedcontainers import SortedList as sl
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        
        s = sl()
        for i, n in enumerate(nums):
            if i > k: s.remove(nums[i - k - 1])
                
            pos1 = bisect_left(s, n - t)
            pos2 = bisect_right(s, n + t)
            
            if pos1 != pos2:
                return True
            
            s.add(nums[i])
        return False
        
 #  IMPLEMENTATION 2
 #  Given below is an implementation in O(n)
 #  The solution uses bucket sort 
 
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for i, n in enumerate(nums):
            buck = n // width
            if buck in buckets:
                return True
            buckets[buck] = n
            if buck+1 in buckets and (buckets[buck+1] - n) <= t:
                return True
            if buck-1 in buckets and (n - buckets[buck-1]) <= t:
                return True
            if i >= k:
                del buckets[nums[i - k] // width]
        return False


 
