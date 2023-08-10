# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)-1

        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return True

            if nums[l]<nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            elif nums[l]>nums[m]:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else:
                l+=1

        return False
    

s=Solution()

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
print(s.search([2,5,6,0,0,1,2], 0))

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
print(s.search[2,5,6,0,0,1,2], 3())