# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # myHash={}

        # for i in nums:
        #     if myHash.get(i,0)==0:
        #         myHash[i]=1
        #     else:
        #         return i

        # Using XOR

        ans=0
        for i in range(1,len(nums)):
            ans^=i
        for i in nums:
            ans^=i
        return ans


s=Solution()

# Input: nums = [1,3,4,2,2]
# Output: 2
print(s.findDuplicate([1,3,4,2,2]))