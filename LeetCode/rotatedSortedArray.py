# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                return mid
            elif nums[s]<=nums[mid]:
                if nums[s]<=target<=nums[mid]:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if nums[mid]<=target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1

        return -1

s=Solution()
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
print(s.search([4,5,6,7,0,1,2],0))