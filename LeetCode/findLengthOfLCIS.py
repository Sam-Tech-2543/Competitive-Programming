# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            l=i
            c=0
            while(l<len(nums)-1):
                if nums[l]<nums[l+1]:
                    c+=1
                else:
                    break
                l+=1
            ans=max(ans,c+1)

        return ans


s=Solution()


# Input: nums = [1,3,5,4,7]
# Output: 3
print(s.findLengthOfLCIS([1,3,5,4,7]))

# Input: nums = [2,2,2,2,2]
# Output: 1
print(s.findLengthOfLCIS([2,2,2,2,2]))
