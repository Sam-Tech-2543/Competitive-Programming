# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lst=set()

        l=0
        for r in range(len(nums)):
            if r-l>k:
                lst.remove(nums[l])
                l+=1
            if nums[r] in lst:
                return True
            lst.add(nums[r])

        return False
    

s=Solution()

# Input: nums = [1,2,3,1], k = 3
# Output: true
print(s.containsNearbyDuplicate([1,2,3,1],3))

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))