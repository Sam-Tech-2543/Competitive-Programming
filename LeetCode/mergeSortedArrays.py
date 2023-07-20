# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last=m+n-1

        m-=1
        n-=1

        while m>=0 and n>=0:
            if nums1[m]<nums2[n]:
                nums1[last]=nums2[n]
                last-=1
                n-=1
            else:
                nums1[last]=nums1[m]
                m-=1
                last-=1

        while n>=0:
            nums1[last]=nums2[n]
            last-=1
            n-=1



s=Solution()

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
s.merge([1,2,3,0,0,0],3,[2,5,6],3)

# Input: nums1 = [2,0], m = 1, nums2 = [1], n = 1
# Output: [1,2]
s.merge([2,0],1,[1],1)